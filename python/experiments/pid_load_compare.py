import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import matplotlib.pyplot as plt

from motor import Motor
from pid import PID
from metrics import step_metrics


dt = 0.001
T = 20.0
setpoint = 1.0
load_torque = 0.01
n = int(T / dt)

controllers = [
    ("P only: Ki = 0", 10.0, 0.0, 0.0),
    ("PI: Ki = 2", 10.0, 2.0, 0.0),
]

fig, ax = plt.subplots(figsize=(9, 6))

for label, kp, ki, kd in controllers:
    motor = Motor(load_torque=load_torque)
    pid = PID(kp=kp, ki=ki, kd=kd)

    t = np.zeros(n)
    theta = np.zeros(n)

    for k in range(1, n):
        voltage = pid.update(setpoint, motor.theta, dt)
        motor.step(voltage, dt)

        t[k] = t[k - 1] + dt
        theta[k] = motor.theta

    metrics = step_metrics(t, theta, setpoint)

    print(f"\n{label}")
    print(f"  Final position: {theta[-1]:.6f} rad")
    print(f"  Steady-state error: {metrics['steady_state_error']:.6f} rad")
    print(f"  Final voltage: {voltage:.4f} V")

    ax.plot(t, theta, label=label)

ax.axhline(setpoint, color="black", linestyle="--", label="Setpoint = 1 rad")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Position θ (rad)")
ax.set_title(f"Constant load disturbance: load torque = {load_torque} N m")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig("results/pid_load_compare.png")
plt.show()
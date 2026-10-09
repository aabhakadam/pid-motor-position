import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import matplotlib.pyplot as plt

from motor import Motor
from pid import PID
from metrics import step_metrics


dt = 0.001
T = 10.0
setpoint = 1.0
n = int(T / dt)

kp_values = [1, 10, 50, 150]

fig, ax = plt.subplots(figsize=(9, 6))

for kp in kp_values:
    motor = Motor()
    pid = PID(kp=kp, ki=0.0, kd=0.0)

    t = np.zeros(n)
    theta = np.zeros(n)

    for k in range(1, n):
        measurement = motor.theta
        voltage = pid.update(setpoint, measurement, dt)
        motor.step(voltage, dt)

        t[k] = t[k - 1] + dt
        theta[k] = motor.theta

    metrics = step_metrics(t, theta, setpoint)

    print(f"\nKp = {kp}")
    print(f"  Rise time: {metrics['rise_time_s']:.4f} s")
    print(f"  Overshoot: {metrics['overshoot_percent']:.2f} %")
    print(f"  Settling time: {metrics['settling_time_s']:.4f} s")
    print(f"  Steady-state error: {metrics['steady_state_error']:.6f} rad")
    print(f"  Final position: {theta[-1]:.6f} rad")
    print(f"  Final voltage: {voltage:.4f} V")

    ax.plot(t, theta, label=f"Kp = {kp}")

ax.axhline(setpoint, color="black", linestyle="--", label="Setpoint = 1 rad")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Position θ (rad)")
ax.set_title("P-only position-control sweep")
ax.set_ylim(-2, 3)
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig("results/pid_p_only_sweep.png")
plt.show()
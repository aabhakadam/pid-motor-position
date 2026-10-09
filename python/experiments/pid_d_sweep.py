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

kp = 50.0
ki = 0.0
kd_values = [0, 1, 5, 10, 20]

fig, ax = plt.subplots(figsize=(9, 6))

for kd in kd_values:
    motor = Motor()
    pid = PID(kp=kp, ki=ki, kd=kd)

    t = np.zeros(n)
    theta = np.zeros(n)

    for k in range(1, n):
        measurement = motor.theta
        voltage = pid.update(setpoint, measurement, dt)
        motor.step(voltage, dt)

        t[k] = t[k - 1] + dt
        theta[k] = motor.theta

    metrics = step_metrics(t, theta, setpoint)

    print(f"\nKp = {kp}, Ki = {ki}, Kd = {kd}")
    print(f"  Rise time: {metrics['rise_time_s']:.4f} s")
    print(f"  Overshoot: {metrics['overshoot_percent']:.2f} %")
    print(f"  Settling time: {metrics['settling_time_s']:.4f} s")
    print(f"  Steady-state error: {metrics['steady_state_error']:.6f} rad")
    print(f"  Final voltage: {voltage:.4f} V")

    ax.plot(t, theta, label=f"Kd = {kd}")

ax.axhline(setpoint, color="black", linestyle="--", label="Setpoint = 1 rad")
ax.set_xlabel("Time (s)")
ax.set_ylabel("Position θ (rad)")
ax.set_title("PD position-control sweep: Kp = 50, Ki = 0")
ax.grid(True)
ax.legend()

plt.tight_layout()
plt.savefig("results/pid_d_sweep.png")
plt.show()
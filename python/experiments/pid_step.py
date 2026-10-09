import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import matplotlib.pyplot as plt

from motor import Motor
from pid import PID


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
        V = pid.update(setpoint, measurement, dt)
        motor.step(V, dt)

        t[k] = t[k - 1] + dt
        theta[k] = motor.theta

    ax.plot(t, theta, label=f"Kp = {kp}")

    print(f"Kp = {kp}")
    print("  Final position:", theta[-1])
    print("  Final voltage:", V)

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
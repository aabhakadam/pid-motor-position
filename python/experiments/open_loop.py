import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import matplotlib.pyplot as plt
from motor import Motor

dt = 0.001
T = 5.0
V = 1.0
n = int(T / dt)

motor = Motor()

t = np.zeros(n)
theta = np.zeros(n)
omega = np.zeros(n)
i_arr = np.zeros(n)

for k in range(1, n):
    motor.step(V, dt)

    t[k] = t[k - 1] + dt
    theta[k] = motor.theta
    omega[k] = motor.omega
    i_arr[k] = motor.i

print("Final omega:", omega[-1])
print("Final theta:", theta[-1])

fig, ax = plt.subplots(3, 1, figsize=(8, 8), sharex=True)

ax[0].plot(t, theta)
ax[0].set_ylabel("Position θ (rad)")
ax[0].grid(True)

ax[1].plot(t, omega)
ax[1].set_ylabel("Speed ω (rad/s)")
ax[1].grid(True)

ax[2].plot(t, i_arr)
ax[2].set_ylabel("Current i (A)")
ax[2].set_xlabel("Time (s)")
ax[2].grid(True)

plt.tight_layout()
plt.savefig("results/open_loop.png")
plt.show()
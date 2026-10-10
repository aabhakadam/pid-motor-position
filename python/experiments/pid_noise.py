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
noise_std = 0.01
n = int(T / dt)

controllers = [
    ("P only: Kd = 0", 50.0, 0.0, 0.0),
    ("PD: Kd = 20", 50.0, 0.0, 20.0),
]

rng = np.random.default_rng(seed=42)

fig, (ax_position, ax_voltage) = plt.subplots(
    2, 1, figsize=(9, 8), sharex=True
)

for label, kp, ki, kd in controllers:
    motor = Motor()
    pid = PID(kp=kp, ki=ki, kd=kd)

    t = np.zeros(n)
    theta = np.zeros(n)
    voltage = np.zeros(n)

    for k in range(1, n):
        noisy_measurement = motor.theta + rng.normal(0.0, noise_std)

        voltage[k] = pid.update(
            setpoint,
            noisy_measurement,
            dt,
        )

        motor.step(voltage[k], dt)

        t[k] = t[k - 1] + dt
        theta[k] = motor.theta

    ax_position.plot(t, theta, label=label)
    ax_voltage.plot(t, voltage, label=label)

ax_position.axhline(setpoint, color="black", linestyle="--", label="Setpoint")
ax_position.set_ylabel("True position θ (rad)")
ax_position.set_title("Effect of measurement noise on P and PD control")
ax_position.grid(True)
ax_position.legend()

ax_voltage.set_xlabel("Time (s)")
ax_voltage.set_ylabel("Requested voltage (V)")
ax_voltage.grid(True)
ax_voltage.legend()

plt.tight_layout()
plt.savefig("results/pid_noise.png")
plt.show()
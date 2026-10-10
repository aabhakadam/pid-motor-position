import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))

import numpy as np
import matplotlib.pyplot as plt

from motor import Motor
from pid import PID


dt = 0.001
T = 20.0
setpoint = 5.0
voltage_limit = 2.0
n = int(T / dt)

motor = Motor()
pid = PID(kp=10.0, ki=2.0, kd=0.0)

t = np.zeros(n)
theta = np.zeros(n)
requested_voltage = np.zeros(n)
applied_voltage = np.zeros(n)

for k in range(1, n):
    requested_voltage[k] = pid.update(
    setpoint,
    motor.theta,
    dt,
    output_limit=voltage_limit,
)

    applied_voltage[k] = max(
        -voltage_limit,
        min(voltage_limit, requested_voltage[k]),
    )

    motor.step(requested_voltage[k], dt)

    t[k] = t[k - 1] + dt
    theta[k] = motor.theta

fig, (ax_position, ax_voltage) = plt.subplots(2, 1, figsize=(9, 8), sharex=True)

ax_position.plot(t, theta, label="Position")
ax_position.axhline(setpoint, color="black", linestyle="--", label="Setpoint")
ax_position.set_ylabel("Position θ (rad)")
ax_position.set_title("Integral windup with 2 V saturation")
ax_position.grid(True)
ax_position.legend()

ax_voltage.plot(t, requested_voltage, label="Requested voltage")
ax_voltage.plot(t, applied_voltage, label="Applied voltage (limited)")
ax_voltage.axhline(voltage_limit, color="black", linestyle="--")
ax_voltage.axhline(-voltage_limit, color="black", linestyle="--")
ax_voltage.set_xlabel("Time (s)")
ax_voltage.set_ylabel("Voltage (V)")
ax_voltage.grid(True)
ax_voltage.legend()

plt.tight_layout()
plt.savefig("results/pid_windup.png")
plt.show()
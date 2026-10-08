import numpy as np
import matplotlib.pyplot as plt

# Motor parameters
J, b, K, R, L = 0.01, 0.1, 0.01, 1.0, 0.5

def derivatives(theta, omega, i, V):
    dtheta = omega
    domega = (K * i - b * omega) / J
    di = (V - R * i - K * omega) / L
    return dtheta, domega, di

dt = 0.001
T = 5.0
V = 1.0
n = int(T / dt)

t = np.zeros(n)
theta = np.zeros(n); omega = np.zeros(n); i_arr = np.zeros(n)

for k in range(1, n):
    dtheta, domega, di = derivatives(
        theta[k - 1],
        omega[k - 1],
        i_arr[k - 1],
        V
    )

    theta[k] = theta[k - 1] + dtheta * dt
    omega[k] = omega[k - 1] + domega * dt
    i_arr[k] = i_arr[k - 1] + di * dt

    t[k] = t[k - 1] + dt

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
print("Final omega:", omega[-1])
print("Final theta:", theta[-1])
plt.show()
class Motor:
    def __init__(self, J=0.01, b=0.1, K=0.01, R=1.0, L=0.5):
        self.J = J
        self.b = b
        self.K = K
        self.R = R
        self.L = L

        self.theta = 0.0
        self.omega = 0.0
        self.i = 0.0

    def step(self, V, dt):
        dtheta = self.omega

        domega = (
            self.K * self.i - self.b * self.omega
        ) / self.J

        di = (
            V - self.R * self.i - self.K * self.omega
        ) / self.L

        self.theta = self.theta + dtheta * dt
        self.omega = self.omega + domega * dt
        self.i = self.i + di * dt

        return self.theta
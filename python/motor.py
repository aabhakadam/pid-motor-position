class Motor:
    def __init__(
        self,
        J=0.01,
        b=0.1,
        K=0.01,
        R=1.0,
        L=0.5,
        load_torque=0.0,
    ):
        self.J = J
        self.b = b
        self.K = K
        self.R = R
        self.L = L
        self.load_torque = load_torque

        self.theta = 0.0
        self.omega = 0.0
        self.i = 0.0

    def step(self, V, dt, voltage_limit=None):
        if voltage_limit is not None:
            V = max(-voltage_limit, min(voltage_limit, V))

        dtheta = self.omega

        domega = (
            self.K * self.i
            - self.b * self.omega
            - self.load_torque
        ) / self.J

        di = (
            V
            - self.R * self.i
            - self.K * self.omega
        ) / self.L

        self.theta = self.theta + dtheta * dt
        self.omega = self.omega + domega * dt
        self.i = self.i + di * dt

        return self.theta
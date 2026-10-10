class PID:
    def __init__(self, kp, ki, kd):
        self.kp = kp
        self.ki = ki
        self.kd = kd

        self.integral = 0.0
        self.prev_error = None

    def update(self, setpoint, measurement, dt, output_limit=None):
        error = setpoint - measurement

        if self.prev_error is None:
            derivative = 0.0
        else:
            derivative = (error - self.prev_error) / dt

        candidate_integral = self.integral + error * dt

        unsaturated_output = (
            self.kp * error
            + self.ki * candidate_integral
            + self.kd * derivative
        )

        if output_limit is None:
            self.integral = candidate_integral
            output = unsaturated_output

        else:
            output = max(
                -output_limit,
                min(output_limit, unsaturated_output),
            )

            saturated_high = output >= output_limit
            saturated_low = output <= -output_limit

            pushes_higher = saturated_high and error > 0
            pushes_lower = saturated_low and error < 0

            if not (pushes_higher or pushes_lower):
                self.integral = candidate_integral

                output = (
                    self.kp * error
                    + self.ki * self.integral
                    + self.kd * derivative
                )

                output = max(
                    -output_limit,
                    min(output_limit, output),
                )

        self.prev_error = error

        return output
#include "pid.hpp"

#include <algorithm>

PID::PID(double kp, double ki, double kd)
    : kp(kp),
      ki(ki),
      kd(kd),
      integral(0.0),
      prev_error(0.0),
      has_prev_error(false) {
}

double PID::update(
    double setpoint,
    double measurement,
    double dt,
    double output_limit
) {
    const double error = setpoint - measurement;

    double derivative = 0.0;

    if (has_prev_error) {
        derivative = (error - prev_error) / dt;
    }

    const double candidate_integral = integral + error * dt;

    const double unsaturated_output =
        kp * error
        + ki * candidate_integral
        + kd * derivative;

    double output = unsaturated_output;

    if (output_limit > 0.0) {
        output = std::clamp(
            unsaturated_output,
            -output_limit,
            output_limit
        );

        const bool saturated_high = output >= output_limit;
        const bool saturated_low = output <= -output_limit;

        const bool pushes_higher = saturated_high && error > 0.0;
        const bool pushes_lower = saturated_low && error < 0.0;

        if (!(pushes_higher || pushes_lower)) {
            integral = candidate_integral;

            output =
                kp * error
                + ki * integral
                + kd * derivative;

            output = std::clamp(
                output,
                -output_limit,
                output_limit
            );
        }
    } else {
        integral = candidate_integral;
    }

    prev_error = error;
    has_prev_error = true;

    return output;
}
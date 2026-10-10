#include "motor.hpp"

#include <algorithm>

Motor::Motor(
    double J,
    double b,
    double K,
    double R,
    double L,
    double load_torque
)
    : theta(0.0),
      omega(0.0),
      current(0.0),
      J(J),
      b(b),
      K(K),
      R(R),
      L(L),
      load_torque(load_torque) {
}

double Motor::step(double voltage, double dt, double voltage_limit) {
    if (voltage_limit > 0.0) {
        voltage = std::clamp(
            voltage,
            -voltage_limit,
            voltage_limit
        );
    }

    const double dtheta = omega;

    const double domega = (
        K * current
        - b * omega
        - load_torque
    ) / J;

    const double dcurrent = (
        voltage
        - R * current
        - K * omega
    ) / L;

    theta = theta + dtheta * dt;
    omega = omega + domega * dt;
    current = current + dcurrent * dt;

    return theta;
}
#ifndef MOTOR_HPP
#define MOTOR_HPP

class Motor {
public:
    Motor(
        double J = 0.01,
        double b = 0.1,
        double K = 0.01,
        double R = 1.0,
        double L = 0.5,
        double load_torque = 0.0
    );

    double step(double voltage, double dt, double voltage_limit = -1.0);

    double theta;
    double omega;
    double current;

private:
    double J;
    double b;
    double K;
    double R;
    double L;
    double load_torque;
};

#endif
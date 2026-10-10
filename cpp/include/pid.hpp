#ifndef PID_HPP
#define PID_HPP

class PID {
public:
    PID(double kp, double ki, double kd);

    double update(
        double setpoint,
        double measurement,
        double dt,
        double output_limit = -1.0
    );

private:
    double kp;
    double ki;
    double kd;

    double integral;
    double prev_error;
    bool has_prev_error;
};

#endif
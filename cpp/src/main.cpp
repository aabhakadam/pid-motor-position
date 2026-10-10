#include <fstream>
#include <iostream>

#include "motor.hpp"
#include "pid.hpp"

int main() {
    const double dt = 0.001;
    const double T = 10.0;
    const double setpoint = 1.0;
    const int steps = static_cast<int>(T / dt);

    Motor motor;
    PID pid(10.0, 0.0, 0.0);

    std::ofstream output("cpp/results/p_only_kp_10.csv");

    if (!output.is_open()) {
        std::cerr << "Could not open output file.\n";
        return 1;
    }

    output << "time,theta,voltage\n";

    double time = 0.0;
    double voltage = 0.0;

    for (int k = 0; k < steps; ++k) {
        voltage = pid.update(setpoint, motor.theta, dt);
        motor.step(voltage, dt);

        output << time << ","
               << motor.theta << ","
               << voltage << "\n";

        time += dt;
    }

    std::cout << "Final position: " << motor.theta << " rad\n";
    std::cout << "Final voltage: " << voltage << " V\n";
    std::cout << "Wrote cpp/results/p_only_kp_10.csv\n";

    return 0;
}
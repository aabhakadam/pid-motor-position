# Stage 5: Saturation and integral windup

## Setup

- Controller: Kp = 10, Ki = 2, Kd = 0
- Setpoint: 5 rad
- Voltage limit: +/-2 V
- Simulation time: 20 s

## Observation

The controller requested about 50 V at the start and about 136 V by the end, but the motor received only +2 V because of saturation. The position was still below the 5 rad setpoint after 20 seconds.

This is integral windup: the integral term continues accumulating positive error while the voltage limit prevents the motor from receiving the requested command. The stored integral action could cause overshoot once the motor reaches the setpoint.
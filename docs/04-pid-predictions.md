# Stage 4 predictions

## Experiment A: D sweep
With Kp = 50 and Ki = 0, increasing Kd should reduce overshoot and ringing because D opposes a rapidly changing error. I expect settling time to improve at first. Very large Kd may make the response slower or cause numerical/noise sensitivity.
## Experiment A: derivative sweep prediction

With Kp = 50 and Ki = 0, I predict that increasing Kd from 0 to a moderate value will reduce overshoot and settling time by damping the oscillation. I expect Kd = 0 to have the largest overshoot, while Kd = 5 or Kd = 10 may be the best trade-off. I predict that a very high Kd such as 20 may slow the response or behave poorly because it strongly reacts to rapid error changes.
## Experiment A: derivative sweep observed

The prediction was mostly correct. Increasing Kd reduced overshoot and ringing:
- Kd = 0: about 57% overshoot and 7.7 s settling time.
- Kd = 5: 33.37% overshoot and 3.63 s settling time.
- Kd = 10: 16.19% overshoot and 2.52 s settling time.
- Kd = 20: 0% overshoot and 1.52 s settling time.

For this ideal noise-free model, Kd = 20 gave the best response: no overshoot and the shortest settling time. My prediction that very high Kd might behave poorly was not supported within this tested range.
## Experiment B: I sweep
With Kp = 10 and Kd = 0, P-only already reaches the step target, so Ki is not needed to remove a steady-state error in this no-load simulation. I predict increasing Ki will mostly add overshoot and ringing because the accumulated past error continues driving the motor after it reaches the target.
## Experiment B: integral sweep prediction

With Kp = 10 and Kd = 0, I predict that increasing Ki will not materially improve the already near-zero steady-state error for this zero-load step response. Instead, the accumulated error will continue contributing after the motor approaches the setpoint, so higher Ki should increase overshoot, oscillation, and possibly settling time.

I predict Ki = 0 will be the cleanest response in this experiment. Ki = 0.5 may add a small overshoot, Ki = 2 may ring more, and Ki = 5 may have the most oscillation or may fail to settle within 10 seconds.
## Experiment B: integral sweep observed

The results supported the prediction. P-only control at Ki = 0 already had near-zero final error. Increasing Ki increased overshoot:
- Ki = 0.5: 13.08% overshoot.
- Ki = 2: 27.90% overshoot.
- Ki = 5: 51.91% overshoot.

For every Ki above zero, settling time was nan because the response was still outside the ±2% band at 10 seconds. This experiment shows that I action is not needed for the zero-load reference step, but it may be necessary later to reject a constant load disturbance.
## Constant-load comparison observed

With load_torque = 0.01 N m:
- P-only control (Kp = 10, Ki = 0) settled at 0.900000 rad, leaving a 0.100000 rad steady-state error.
- PI control (Kp = 10, Ki = 2) reached 1.001303 rad, leaving only -0.001303 rad error after 20 seconds.

This shows why integral action matters: it accumulates the persistent error caused by the constant load and supplies the voltage needed to reject that disturbance.
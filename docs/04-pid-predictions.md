# Stage 4 predictions

## Experiment A: D sweep
With Kp = 50 and Ki = 0, increasing Kd should reduce overshoot and ringing because D opposes a rapidly changing error. I expect settling time to improve at first. Very large Kd may make the response slower or cause numerical/noise sensitivity.
## Experiment A: derivative sweep prediction

With Kp = 50 and Ki = 0, I predict that increasing Kd from 0 to a moderate value will reduce overshoot and settling time by damping the oscillation. I expect Kd = 0 to have the largest overshoot, while Kd = 5 or Kd = 10 may be the best trade-off. I predict that a very high Kd such as 20 may slow the response or behave poorly because it strongly reacts to rapid error changes.
## Experiment B: I sweep
With Kp = 10 and Kd = 0, P-only already reaches the step target, so Ki is not needed to remove a steady-state error in this no-load simulation. I predict increasing Ki will mostly add overshoot and ringing because the accumulated past error continues driving the motor after it reaches the target.
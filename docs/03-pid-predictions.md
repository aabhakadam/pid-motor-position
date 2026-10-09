# P-only PID predictions

Setpoint: 1 rad
Ki = 0
Kd = 0

## Kp = 1
- Rise compared with open loop: Faster because the controller applies voltage when position error exists, but still slow.
- Overshoot: Probably no noticeable overshoot.
- Does it settle: Yes, but slowly.

## Kp = 10
- Rise compared with Kp = 1: Faster.
- Overshoot: Small overshoot may begin.
- Does it settle: Probably yes, after some small correction.

## Kp = 50
- Rise compared with Kp = 10: Much faster.
- Overshoot: Likely noticeable overshoot and wobbling around 1 rad.
- Does it settle: It may settle, but more slowly because of oscillations.

## Kp = 150
- Rise compared with Kp = 50: Very fast and aggressive.
- Overshoot: Likely large overshoot and strong oscillation.
- Does it settle: It may become unstable or take a long time to settle.
## Results and comparison

- Kp = 1: My prediction was correct. The response was slow, had no overshoot, and did not reach 1 rad within 10 s.
- Kp = 10: My prediction was mostly correct. It was much faster, had very small overshoot, and settled close to 1 rad.
- Kp = 50: My prediction was correct. It reached the target quickly but overshot and oscillated before settling.
- Kp = 150: My prediction was correct. The oscillations increased instead of decreasing, so the system was unstable and did not settle.
- Best P-only value from this sweep: Kp = 10, because it reached the setpoint quickly with very little oscillation.
## Predicted versus observed

- Kp = 1: I predicted a slow, stable response without overshoot. Observed: correct; it reached about 0.63 rad after 10 s, so it was still approaching 1 rad.
- Kp = 10: I predicted a faster response with little or no overshoot. Observed: mostly correct; it had about 9% overshoot and settled very close to 1 rad.
- Kp = 50: I predicted a faster response with overshoot and oscillation. Observed: correct; it overshot by about 58% and rang around the setpoint.
- Kp = 150: I predicted instability or strong oscillation. Observed: correct; its oscillations grew instead of decaying, so it did not settle.
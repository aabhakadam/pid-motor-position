# Open-loop predictions (V = 1 V, from rest)

## Steady state
- omega_ss = 0.0999 rad/s
- i_ss = 0.999 A
- At steady state, motor torque and friction torque balance:
  K * i = 0.01 * 0.999 = 0.00999
  b * omega = 0.1 * 0.0999 = 0.00999

## Time scales
- tau_slow = 0.5 s
- tau_fast = 0.1 s
- The pole at -2 dominates because it has the larger time constant, so it decays more slowly.
- The pole at -10 disappears faster because its time constant is only 0.1 s.
- Settling time is approximately 4 * tau_slow = 2 s.

## Expected plot shapes
- omega starts at zero, rises smoothly, and levels off near 0.0999 rad/s after about 2 s.
- i starts at zero, rises smoothly, and levels off near 0.999 A.
- The initial current slope is V / L = 1 / 0.5 = 2 A/s.
- theta curves upward during the first roughly 2 s while speed increases.
- After speed becomes constant, theta becomes almost a straight line with slope 0.0999 rad/s.

## Mistakes I made while predicting
- I initially got omega_ss = 9.99 because I did not correctly include the friction term in the steady-state calculation.
- I first said the -10 pole dominates. This was wrong because it decays faster; the -2 pole is slower and therefore sets the settling time.
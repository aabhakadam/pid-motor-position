import numpy as np

# MY PREDICTION (write before running): are the poles real or complex? roughly where?
# ...

poles = np.roots([0.005, 0.06, 0.1001])
dc_gain = 0.01 / 0.1001

print("poles:", poles)
print("DC gain (rad/s per volt):", dc_gain)
import math
from pid import PID


# Test 1: P-only controller
pid = PID(kp=3.0, ki=0.0, kd=0.0)
result = pid.update(setpoint=1.0, measurement=0.0, dt=0.001)

assert math.isclose(result, 3.0)
print("Test 1 passed: P-only")


# Test 2: I-only controller
pid = PID(kp=0.0, ki=2.0, kd=0.0)

first_result = pid.update(setpoint=1.0, measurement=0.0, dt=0.001)
second_result = pid.update(setpoint=1.0, measurement=0.0, dt=0.001)

expected = 2.0 * (1.0 * 0.001 + 1.0 * 0.001)

assert math.isclose(first_result, 0.002)
assert math.isclose(second_result, expected)
print("Test 2 passed: I-only")


# Test 3: D-only controller
pid = PID(kp=0.0, ki=0.0, kd=4.0)

first_result = pid.update(setpoint=1.0, measurement=0.0, dt=0.001)
second_result = pid.update(setpoint=1.0, measurement=0.5, dt=0.001)

expected = 4.0 * (-0.5 / 0.001)

assert math.isclose(first_result, 0.0)
assert math.isclose(second_result, expected)
print("Test 3 passed: D-only")

print("All PID tests passed.")
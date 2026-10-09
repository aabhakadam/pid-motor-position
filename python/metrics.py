import numpy as np


def step_metrics(t, y, setpoint):
    """Return standard step-response metrics."""

    t = np.asarray(t, dtype=float)
    y = np.asarray(y, dtype=float)

    if t.ndim != 1 or y.ndim != 1:
        raise ValueError("t and y must be one-dimensional arrays")

    if len(t) != len(y):
        raise ValueError("t and y must have the same length")

    if len(t) < 2:
        raise ValueError("t and y must contain at least two samples")

    if setpoint == 0:
        raise ValueError("setpoint must be non-zero for percentage metrics")

    direction = 1 if setpoint > 0 else -1
    response = direction * y
    target = abs(setpoint)

    peak = np.max(response)
    overshoot_percent = max(0.0, (peak - target) / target * 100.0)

    t_10 = 0.1 * target
    t_90 = 0.9 * target

    i_10 = np.flatnonzero(response >= t_10)
    i_90 = np.flatnonzero(response >= t_90)

    if len(i_10) == 0 or len(i_90) == 0:
        rise_time = np.nan
    else:
        rise_time = t[i_90[0]] - t[i_10[0]]

    tolerance = 0.02 * target
    outside_band = np.flatnonzero(np.abs(response - target) > tolerance)

    if len(outside_band) == 0:
        settling_time = 0.0
    elif outside_band[-1] == len(t) - 1:
        settling_time = np.nan
    else:
        settling_time = t[outside_band[-1] + 1]

    steady_state_error = setpoint - y[-1]

    return {
        "rise_time_s": rise_time,
        "overshoot_percent": overshoot_percent,
        "settling_time_s": settling_time,
        "steady_state_error": steady_state_error,
    }
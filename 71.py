# TASK 71

from math import sin

eps, a, b = 0.002, 1, 1.5

while abs(a - b) > eps:
    fa = a * sin(a - 1)
    m = round((a + b) / 2, 4)
    fm = m * sin(m - 1)
    if fa * fm >= 0:
        a = m
    else:
        b = m

print(a)

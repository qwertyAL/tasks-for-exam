# TASK 70

from math import cos

eps, a, b = 0.0001, 0, 1

while abs(a - b) > eps:
    fa = cos(a) - a
    m = round((a + b) / 2, 4)
    fm = cos(m) - m
    if fa * fm >= 0:
        a = m
    else:
        b = m

print(b)

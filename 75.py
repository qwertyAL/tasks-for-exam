# TASK 74
# y = x ** 2 + 4

from math import pi, sin

a, b, e = 0, pi, 0.0001

ans = 0

while a <= b:
    a1 = a
    a2 = a + e
    f1 = sin(a1)
    f2 = sin(a2)
    s = (f1 + f2) * e / 2
    ans += s
    a += e

print(ans)

# TASK 73

from random import randint
from math import pi, sin

a = 0
b = pi
n = 10000

maxY = 0
for i in range(a, round(b + 1)):
    maxY = max(maxY, sin(i))

k = 0
for i in range(10001):
    x = randint(a, round(b))
    y = randint(0, round(maxY))
    trueY = sin(x)
    if y <= trueY:
        k += 1

c = k / n
ans = (b - a) * maxY * c
print(ans)

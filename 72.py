# TASK 72
# y = x**2 + 4 a = -2 b = 2 n = 10000

from random import randint

a, b = -2, 2
n = 10000
k = 0

maxY = 0
for i in range(a, b + 1):
    maxY = max(maxY, i * i + 4)

for i in range(10001):
    x = randint(a, b)
    y = randint(0, maxY)

    trueY = x * x + 4

    if y <= trueY:
        k += 1

c = k / n
ans = (b - a) * maxY * c

print(ans)

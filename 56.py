# TASK 56
# input: a, b, c
# output: x1, x2 / x / none

from math import sqrt

a, b, c = map(int, input().split())

d = b ** 2 - 4 * a * c

if d < 0:
    print("none")
elif d == 0:
    print((-b + sqrt(d)) / 2 / a)
else:
    print((-b + sqrt(d)) / 2 / a, (-b - sqrt(d)) / 2 / a)

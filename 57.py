# TASK 57
# input: a, b, c, d

a, b, c, d = map(int, input().split())

for x in range(1001):
    f = a * x ** 3 + b * x ** 2 + c * x + d
    if f == 0:
        print(x)

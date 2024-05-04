# TASK 74
# y = x ** 2 + 4

a, b, e = -2, 2, 0.0001

ans = 0

while a <= b:
    a1 = a
    a2 = a + e
    f1 = a1 ** 2 + 4
    f2 = a1 ** 2 + 4
    s = (f1 + f2) * e / 2
    ans += s
    a += e

print(ans)

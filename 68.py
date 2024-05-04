# TASK 68

ans = 0
x = 39.7

for i in range(7):
    if i == 0:
        ans += 39
    elif i == 2:
        ans -= 45
    elif i == 6:
        ans += 4.9
    ans *= x

print("ans:", round(ans, 4))

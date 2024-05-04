# TASK 69

ans = 0
x = 11.11

for i in range(14):
    if i == 0:
        ans += 19
    elif i == 4:
        ans += 17
    elif i == 5:
        ans += 0.7
    elif i == 11:
        ans -= 1.7
    elif i == 13:
        ans -= 119
    ans *= x
ans += 15

print("ans:", round(ans, 4))

# TASK 60

n = int(input())

x = 2
ans = False
while x <= n:
    if n == x:
        ans = True
        break
    x *= 2

if ans:
    print("YES")
else:
    print("NO")

# TASK 62

l = list(map(int, input().split()))
n = int(input())

ans = 0
for el in l:
    if el == n:
        ans += 1

print(ans)

# TASK 59

n = int(input())

ans = 2

while n % ans != 0:
    if ans ** 2 > n:
        ans = n
        break
    ans += 1

print(ans)

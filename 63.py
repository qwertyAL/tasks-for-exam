# TASK 63

l = list(map(int, input().split()))

minEl = l[0]
for el in l:
    if el < minEl:
        minEl = el

ans = 0
for el in l:
    if el == minEl:
        ans += 1

print("min:", minEl)
print("count:", ans)

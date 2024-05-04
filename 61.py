# TASK 61

l = list(map(int, input().split()))

minEl = l[0]
maxEl = l[0]

for el in l:
    if el < minEl:
        minEl = el
    
    if el > maxEl:
        maxEl = el

print("min:", minEl)
print("max:", maxEl)

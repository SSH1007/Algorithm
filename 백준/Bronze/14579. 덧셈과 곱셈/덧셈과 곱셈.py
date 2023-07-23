a, b = map(int, input().split())
dap = 1
for i in range(a, b+1):
    tmp = 0
    for j in range(1, i+1):
        tmp += j
    dap *= tmp
print(dap % 14579)
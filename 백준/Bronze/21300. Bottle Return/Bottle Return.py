lst = list(map(int, input().split()))
lst = [l for l in lst if l!=0]
dap = 0
for l in lst:
    dap+=(l*5)
print(dap)
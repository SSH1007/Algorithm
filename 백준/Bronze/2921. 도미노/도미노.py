N = int(input())
dap = 0
for i in range(N+1):
    for j in range(N+1):
        if i<=j:
            dap+=(i+j)
print(dap)
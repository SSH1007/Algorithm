N = int(input())
dap = 0
for n in range(1, N+1):
    for m in range(n, N//n+1):
        dap += 1
print(dap)
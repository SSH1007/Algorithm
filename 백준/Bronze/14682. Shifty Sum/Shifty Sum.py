N = int(input())
k = int(input())
dap = N
for i in range(1, k+1):
    dap += N*(10**i)
print(dap)
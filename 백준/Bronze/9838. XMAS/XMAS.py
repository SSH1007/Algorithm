N = int(input())
dap = [0]*N
for n in range(N):
    k = int(input())
    dap[k-1] = n+1
for d in dap:
    print(d)
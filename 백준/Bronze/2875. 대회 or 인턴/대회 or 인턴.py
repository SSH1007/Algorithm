N, M, K = map(int,input().split())
dap = 0
for i in range(K+1):
    tmp = min((N-i)//2, M-(K-i))
    if dap <= tmp:
        dap = tmp
print(dap)
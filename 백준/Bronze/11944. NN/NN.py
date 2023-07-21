N, M = map(int, input().split())
dap = str(N)*N
if len(dap) >= M:
    print(dap[:M])
else:
    print(dap)
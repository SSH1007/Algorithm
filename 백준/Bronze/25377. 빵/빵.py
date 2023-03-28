N = int(input())
inf = int(1e9)
dap = inf
for _ in range(N):
    A, B = map(int, input().split())
    if A<=B:
        dap = min(dap, B)
if dap == inf:
    print(-1)
else:    
    print(dap)
import sys
input = lambda: sys.stdin.readline().rstrip()


V, E = map(int, input().split())
inf = float('inf')
maps = [[inf]*(V+1) for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    maps[a][b] = c

for k in range(1, V+1):
    for i in range(1, V+1):
        for j in range(1, V+1):
            maps[i][j] = min(maps[i][j], maps[i][k]+maps[k][j])

dap = inf
for i in range(1, V+1):
    for j in range(1, V+1):
        if i == j:
            dap = min(dap, maps[i][j])
if dap == inf:
    print(-1)
else:
    print(dap)
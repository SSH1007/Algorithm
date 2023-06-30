import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
dap = []

def bfs(n, m):
    q = deque([(n, m)])
    graph[n][m] = 0
    size = 1
    while q:
        sn, sm = q.popleft()
        for dn, dm in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            nn = sn + dn
            nm = sm + dm
            if 0 <= nn < N and 0 <= nm < M and graph[nn][nm]:
                q.append((nn, nm))
                graph[nn][nm] = 0
                size += 1
    dap.append(size)

for n in range(N):
    for m in range(M):
        if graph[n][m]:
            bfs(n, m)

if dap:
    print(len(dap))
    print(max(dap))
else:
    print(0)
    print(0)
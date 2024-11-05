import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
from itertools import combinations as comb

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def BFS(V):
    q = deque(V)
    for v in V:
        visited[v[0]][v[1]] = 0
    tmp = 0
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == -1 and maps[nr][nc] != 1:
                    q.append((nr, nc))
                    visited[nr][nc] = visited[r][c] + 1

    for i in range(N):
        for j in range(N):
            if maps[i][j] != 1 and visited[i][j] == -1:
                return inf
            tmp = max(tmp, visited[i][j])
    return tmp


inf = float('inf')
dap = inf
N, M = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
virus = []
for i in range(N):
    for j in range(N):
        if maps[i][j] == 2:
            virus.append((i, j))

for c in comb(virus, M):
    visited = [[-1]*N for _ in range(N)]
    dap = min(dap, BFS(c))
if dap == inf:
    print(-1)
else:
    print(dap)
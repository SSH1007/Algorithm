import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().split())
planet = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 탐사 지점 찾기
point = []
for i in range(N):
    for j in range(M):
        if not planet[i][j]:
            point.append((i, j))

# 델타탐색
dx = [0,-1,0,1]
dy = [-1,0,1,0]


def BFS(r, c):
    q = deque([(r, c)])
    visited[r][c] = 1
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = (cr + dy[i])%N
            nc = (cc + dx[i])%M
            if not visited[nr][nc] and planet[nr][nc] != 1:
                visited[nr][nc] = 1
                q.append((nr, nc))
    return 1

dap = 0
for n, m in point:
    if not visited[n][m]:
        dap += BFS(n, m)

print(dap)
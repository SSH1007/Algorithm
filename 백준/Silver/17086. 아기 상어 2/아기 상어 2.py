import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().rstrip().split())
sea = [list(map(int, input().rstrip().split())) for _ in range(N)]
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
dap = 0


def BFS(i, j):
    visited = [[0]*M for _ in range(N)]
    q = deque([(i, j)])
    visited[i][j] = 1
    while q:
        r, c = q.popleft()
        if sea[r][c] == 1:
            return visited[r][c]-1
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
    return 0


for n in range(N):
    for m in range(M):
        if not sea[n][m]:
            dap = max(dap, BFS(n, m))
print(dap)
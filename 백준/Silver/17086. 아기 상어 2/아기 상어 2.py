import sys
input = sys.stdin.readline
from collections import deque
N, M = map(int, input().rstrip().split())
sea = [list(map(int, input().rstrip().split())) for _ in range(N)]
dr = [-1, -1, -1, 0, 0, 1, 1, 1]
dc = [-1, 0, 1, -1, 1, -1, 0, 1]
dap = 0
q = deque()
# 시작 시점에 상어들의 위치 큐에 삽입
for i in range(N):
    for j in range(M):
        if sea[i][j]:
            q.append((i, j))


def BFS():
    while q:
        r, c = q.popleft()
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if not sea[nr][nc]:
                    sea[nr][nc] = sea[r][c] + 1
                    q.append((nr, nc))
    return 0


BFS()
for s in sea:
    dap = max(max(s), dap)
print(dap-1)
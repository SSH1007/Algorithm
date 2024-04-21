import sys
input = sys.stdin.readline
from collections import deque
M, N = map(int, input().rstrip().split())
data = [list(map(int, list(input().rstrip()))) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
starts = [i for i in range(N) if data[0][i] == 0]
dr = [0, -1, 0, 1]
dc = [1, 0, -1, 0]


def BFS(c):
    q = deque([(0, c)])
    while q:
        r, c = q.popleft()
        if r == M-1:
            return 1
        visited[r][c] = 1
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < M and 0 <= nc < N:
                if not visited[nr][nc] and not data[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
    return 0


dap = 0
for s in starts:
    dap = max(BFS(s), dap)
if dap:
    print('YES')
else:
    print('NO')
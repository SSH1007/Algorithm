import sys
input = sys.stdin.readline
from collections import deque


def BFS(r, c):
    answer = 1
    q = deque([(r, c)])
    grid[r][c] = 2
    while q:
        r, c = q.popleft()
        for dr, dc in [(1, 0), (0, 1), (-1, 0), (0, -1)]:
            nr = r + dr
            nc = c + dc
            if 0 <= nr < M and 0 <= nc < N:
                if not grid[nr][nc]:
                    grid[nr][nc] = 2
                    answer += 1
                    q.append((nr, nc))
    return answer


M, N, K = map(int, input().rstrip().split())
grid = [[0]*N for _ in range(M)]
dap = []
for _ in range(K):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    for x in range(x1, x2):
        for y in range(y1, y2):
            if not grid[y][x]:
                grid[y][x] = 1

for r in range(M):
    for c in range(N):
        if not grid[r][c]:
            dap.append(BFS(r, c))

print(len(dap))
print(*sorted(dap))
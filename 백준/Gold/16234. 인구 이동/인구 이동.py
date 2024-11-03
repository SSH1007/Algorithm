import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def BFS(r, c):
    # 국경선을 공유하는 두 나라간 인구차가 L~R인지 확인하여 연합 구성
    q = deque([(r, c)])
    union = [(r, c)]
    while q:
        cr, cc = q.popleft()
        for i in range(4):
            nr = cr + dr[i]
            nc = cc + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    if L <= abs(maps[nr][nc]-maps[cr][cc]) <= R:
                        visited[nr][nc] = 1
                        union.append((nr, nc))
                        q.append((nr, nc))

    if len(union) == 1:
        return 0

    # 연합 인구수 파악
    newP = sum(maps[i][j] for i, j in union)//len(union)
    # 인구수 maps 재구성
    for r, c in union:
        maps[r][c] = newP
    return 1


N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dap = 0
while 1:
    visited = [[0]*N for _ in range(N)]
    group = 0
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                visited[r][c] = 1
                group += BFS(r, c)
    if group == 0:
        break
    dap += 1
print(dap)
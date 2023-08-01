import sys
input = sys.stdin.readline
from collections import deque
dx = [0,-1,0,1,1,-1,1,-1]
dy = [-1,0,1,0,1,-1,-1,1]


def BFS(r, c, visited):
    q = deque([(r, c)])
    visited[r][c] = 1
    while q:
        rr, cc = q.popleft()
        for i in range(8):
            nr = rr + dy[i]
            nc = cc + dx[i]
            if 0 <= nr < h and 0 <= nc < w:
                if data[nr][nc] and not visited[nr][nc]:
                    visited[nr][nc] = 1
                    q.append((nr, nc))
    return 1


while 1:
    w, h = map(int, input().rstrip().split())
    if w == 0 and h == 0:
        break
    data = [list(map(int, input().rstrip().split())) for _ in range(h)]
    location = []
    for i in range(h):
        for j in range(w):
            if data[i][j]:
                location.append((i,j))
    cnt = 0
    visited = [[0]*w for _ in range(h)]
    for r, c in location:
        if not visited[r][c]:
            cnt += BFS(r, c, visited)

    print(cnt)
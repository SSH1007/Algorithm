import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def find():
    for i in range(n):
        for j in range(m):
            if As[i][j] == 2:
                visited[i][j] = 0
                return i, j


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
n, m = map(int, input().split())
As = [list(map(int, list(input()))) for _ in range(n)]
visited = [[-1]*m for _ in range(n)]
q = deque([find()])
while q:
    r, c = q.popleft()
    if As[r][c] > 2:
        print('TAK')
        print(visited[r][c])
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < m:
            if visited[nr][nc] == -1 and As[r][c] != 1:
                visited[nr][nc] = visited[r][c] + 1
                q.append((nr, nc))
else:
    print('NIE')
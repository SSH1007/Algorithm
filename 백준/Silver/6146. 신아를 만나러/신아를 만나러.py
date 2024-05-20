import sys
input = sys.stdin.readline
from collections import deque
X, Y, N = map(int, input().rstrip().split())
# (0,0)을 기준으로 상하좌우 500이므로 1001*1001 그래프 생성
# (0,0)은 (500,500)으로, (X,Y)는 (X+500, Y+500)으로
graph = [[0]*1001 for _ in range(1001)]
X, Y = X+500, Y+500
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    graph[b+500][a+500] = -1
# 델타 탐색
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def BFS():
    q = deque([(500, 500)])
    graph[500][500] = 1
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if nr == Y and nc == X:
                print(graph[r][c])
                return
            if 0 <= nr < 1001 and 0 <= nc <= 1001:
                if not graph[nr][nc]:
                    q.append((nr, nc))
                    graph[nr][nc] = graph[r][c] + 1


BFS()
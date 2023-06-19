# bfs 문제 : 14940 쉬운 최단거리
import sys
input = sys.stdin.readline
# 입력
n, m = map(int, input().rstrip().split())
graph = [list(map(int, input().rstrip().split())) for _ in range(n)]
# 일단 전부 갈 수는 있지만 도달할 수 없는 위치로 초기화(-1)
dap = [[-1]*m for _ in range(n)]
# bfs 정의
from collections import deque
def bfs(x,y):
    q = deque([(x,y)])
    dap[x][y] = 0
    while q:
        ox, oy = q.popleft()
        for dx, dy in [(0,-1),(0,1),(-1,0),(1,0)]:
            nx = ox+dx
            ny = oy+dy
            if 0 <= nx < n and 0 <= ny < m and dap[nx][ny] == -1:
                # 원래 갈 수 없는 땅은 0
                if graph[nx][ny] == 0:
                    dap[nx][ny] = 0
                # 갈 수 있는 땅 중, 도달할 수 있는 위치는 계속 append
                elif graph[nx][ny] == 1:
                    dap[nx][ny] = dap[ox][oy]+1
                    q.append((nx, ny))
# bfs 실행
for N in range(n):
    for M in range(m):
        if graph[N][M] == 2 and dap[N][M] == -1:
            bfs(N, M)
# bfs로 가지 않은 땅 중, graph에서 0(갈 수 없는 땅)으로 표기된 곳은 dap에서도 0으로 표시해줘야 한다.
for N in range(n):
    for M in range(m):
        if graph[N][M] == 0:
            dap[N][M] = 0
# 출력
for d in dap:
    print(*d)
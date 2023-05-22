import sys
input = sys.stdin.readline

# BFS 함수 구현
from collections import deque
def BFS(y, x, graph, visit):
    global R, G, B
    que = deque([(y, x)])
    visit[y][x] = 1
    while que:
        y, x = que.popleft()
        for dy, dx in [(-1,0), (1,0), (0,-1), (0,1)]:
            ny, nx = y+dy, x+dx
            if ny >= 0 and ny < N and nx >= 0 and nx < N and visit[ny][nx] == 0:
                if graph[ny][nx] == graph[y][x]:
                    visit[ny][nx] = 1
                    que.append((ny,nx))
    # BFS가 끝나고 RGB 구역의 수 카운팅
    if graph[y][x] == 'R':
        R += 1
    elif graph[y][x] == 'G':
        G += 1
    elif graph[y][x] == 'B':
        B += 1

# 크기 N 입력
N = int(input().rstrip())
# 정상인 테스트
graph1 = [list(input().rstrip()) for _ in range(N)]
R, G, B = 0, 0, 0
visited1 = [[0]*N for _ in range(N)]
# i행(y) j열(x)
for i in range(N):
    for j in range(N):
        if not visited1[i][j]:
            BFS(i, j, graph1, visited1)
print(R + G + B, end=' ')

# 적록색약 테스트
graph2 = []
R, G, B = 0, 0, 0
visited2 = [[0]*N for _ in range(N)]
for i in range(N):
    tmplst = []
    for g in graph1[i]:
        tmp = g.replace('R', 'G')
        tmplst.append(tmp)
    graph2.append(tmplst)
for i in range(N):
    for j in range(N):
        if not visited2[i][j]:
            BFS(i, j, graph2, visited2)
print(R + G + B)
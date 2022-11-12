N = int(input())
sea = [list(map(int, input().split())) for _ in range(N)]
# 아기 상어 크기 초기화
shark_size = 2

# 아기 상어 위치 파악
for i in range(N):
    for j in range(N):
        if sea[i][j] == 9:
            start_x = i
            start_y = j
            sea[i][j]=0
            break

# 조건에 맞는 물고기를 찾는 BFS(최단거리)
def bfs(start_x, start_y):
    from collections import deque
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    visited = [[0]*N for _ in range(N)]
    visited[start_x][start_y] = 1
    q = deque([(start_x,start_y,0)])
    fishes = []

    while q:
        x,y,count = q.popleft()
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            if 0 <= nx < N and 0 <= ny < N and not visited[nx][ny]:
                visited[nx][ny] = 1
                # 공간의 숫자가 0보다 크고 아기 상어 크기보다 작으면 다음 이동 목적지에 포함
                # 먹을 물고기 목록에 포함
                if 0 < sea[nx][ny] < shark_size:
                    q.append((nx,ny,count+1))  
                    fishes.append((nx,ny,count+1))
                # 공간의 숫자가 0이나 아기 상어 크기와 같으면 다음 이동 목적지에 포함
                elif sea[nx][ny] == 0 or sea[nx][ny] == shark_size:
                    q.append((nx,ny,count+1))

    if fishes:
        # 거리, 가장 위, 가장 왼쪽 기준으로 정렬
        return sorted(fishes,key=lambda x:(-x[2],-x[0],-x[1]))
    else:
        return []
    
ate = 0
dap = 0
while 1:
    eatPlace = bfs(start_x,start_y)
    if len(eatPlace):
        start_x, start_y, move = eatPlace.pop()
        sea[start_x][start_y] = 0
        ate += 1
        dap+=move
        if ate == shark_size:
            shark_size+=1
            ate=0
    else:
        break
print(dap)
from collections import deque
def bfs(r,c):
    q = deque([(r,c)])
    bat[r][c] = 0
    dr = [-1,1,0,0]
    dc = [0,0,-1,1]
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r+dr[i]
            nc = c+dc[i]
            if 0<=nr<N and 0<=nc<M and bat[nr][nc]==1:
                bat[nr][nc] = 0
                q.append((nr,nc))

T = int(input())
for _ in range(T):
    dap = 0
    # M : 배추밭 가로 길이 / N : 배추밭 세로 길이 / K : 배추 위치 개수
    M, N, K = map(int, input().split())
    bat = [[0] * (M) for _ in range(N)]
    for k in range(K):
        x, y = map(int, input().split())
        bat[y][x] = 1
    
    for n in range(N):
        for m in range(M):
            if bat[n][m] == 1:
                dap+=1
                bfs(n,m)
    print(dap)
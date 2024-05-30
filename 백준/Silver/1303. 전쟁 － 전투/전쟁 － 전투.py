import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
soldiers = [list(input().rstrip()) for _ in range(M)]
visited = [[0]*N for _ in range(M)]
W, B = 0, 0
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def DFS(r, c, ally):
    global tmp
    tmp += 1
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < M and 0 <= nc < N:
            if not visited[nr][nc] and soldiers[nr][nc] == ally:
                DFS(nr, nc, ally)
    return ally


for m in range(M):
    for n in range(N):
        if not visited[m][n]:
            tmp = 0
            color = DFS(m, n, soldiers[m][n])
            if color == 'W':
                W += (tmp**2)
            else:
                B += (tmp**2)
print(W, B)
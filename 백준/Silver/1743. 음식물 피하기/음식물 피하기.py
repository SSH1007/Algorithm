import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)
N, M, K = map(int, input().rstrip().split())
room = [[0]*M for _ in range(N)]
for _ in range(K):
    r, c = map(int, input().rstrip().split())
    room[r-1][c-1] = 1
visited = [[0]*M for _ in range(N)]

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

dap = 0


def DFS(r, c):
    global size
    visited[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M and not visited[nr][nc] and room[nr][nc]:
            DFS(nr, nc)
            size += 1
    return size


for i in range(N):
    for j in range(M):
        if room[i][j] and not visited[i][j]:
            size = 1
            dap = max(DFS(i, j), dap)
print(dap)
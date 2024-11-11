import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def DFS(r, c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if not visited[nr][nc] and maps[nr][nc]:
                visited[nr][nc] = 1
                DFS(nr, nc)
    return


N, M = map(int, input().split())
lst = [list(map(int, input().split())) for _ in range(N)]
T = int(input())

maps = [[0]*M for _ in range(N)]
for n in range(N):
    for m in range(0, M*3, 3):
        tmp = (lst[n][m]+lst[n][m+1]+lst[n][m+2]) / 3
        if tmp >= T:
            maps[n][m//3] = 255

dap = 0
visited = [[0]*M for _ in range(N)]
for n in range(N):
    for m in range(M):
        if not visited[n][m] and maps[n][m]:
            visited[n][m] = 1
            DFS(n, m)
            dap += 1

print(dap)
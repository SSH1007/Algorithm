import sys
input = lambda: sys.stdin.readline().rstrip()

dap = -10000*100
N, M, K = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]
dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]
visited = [[0]*M for _ in range(N)]


def adj_check(r, c):
    # 인접한 칸이 있으면 True 반환
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < N and 0 <= nc < M:
            if visited[nr][nc]:
                return True
    return False


def DFS(hap, depth, r, c):
    global dap
    if depth == K:
        dap = max(dap, hap)
        return
    for n in range(r, N):
        for m in range(c if n == r else 0, M):
            if visited[n][m]:
                continue
            if adj_check(n, m):
                continue
            visited[n][m] = 1
            DFS(hap+maps[n][m], depth+1, n, m)
            visited[n][m] = 0


DFS(0, 0, 0, 0)
print(dap)
import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
pattern = [input().rstrip() for _ in range(N)]
dap = 0
visited = [[False]*M for _ in range(N)]


def dfs(n, m):
    visited[n][m] = True
    if pattern[n][m] == '|' and n+1 < N:
        if pattern[n+1][m] == '|' and not visited[n+1][m]:
            dfs(n+1, m)
        else:
            return
    elif pattern[n][m] == '-' and m+1 < M:
        if pattern[n][m+1] == '-' and not visited[n][m+1]:
            dfs(n, m+1)
        else:
            return


for n in range(N):
    for m in range(M):
        if not visited[n][m]:
            dfs(n, m)
            dap += 1


print(dap)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n = int(input())
bamboo = [list(map(int, input().rstrip().split())) for _ in range(n)]
dp = [[-1]*n for _ in range(n)]
dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


def DFS(r, c):
    if dp[r][c] != -1:
        return dp[r][c]
    dp[r][c] = 1
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < n and 0 <= nc < n:
            if bamboo[nr][nc] > bamboo[r][c]:
                dp[r][c] = max(dp[r][c], DFS(nr, nc)+1)
    return dp[r][c]


for i in range(n):
    for j in range(n):
        DFS(i, j)
dap = 0
for d in dp:
    dap = max(dap, max(d))
print(dap)
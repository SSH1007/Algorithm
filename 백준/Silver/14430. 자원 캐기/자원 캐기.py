import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
mine = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0]*M for _ in range(N)]
dp[0][0] = mine[0][0]

for n in range(N):
    for m in range(M):
        if 0 <= m-1 <= M:
            dp[n][m] = max(dp[n][m], dp[n][m-1] + mine[n][m])
        if 0 <= n-1 <= N:
            dp[n][m] = max(dp[n][m], dp[n-1][m] + mine[n][m])

print(dp[N-1][M-1])
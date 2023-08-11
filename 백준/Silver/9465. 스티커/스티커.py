import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    dp = [list(map(int, input().rstrip().split())) for _ in range(2)]

    if N >= 2:
        dp[0][1] += dp[1][0]
        dp[1][1] += dp[0][0]
    for n in range(2, N):
        for i in range(2):
            dp[i][n] = max(dp[i][n]+dp[i][n-2], dp[i][n]+dp[abs(i-1)][n-2], dp[i][n]+dp[abs(i-1)][n-1])
    print(max(dp[0][N-1], dp[1][N-1]))
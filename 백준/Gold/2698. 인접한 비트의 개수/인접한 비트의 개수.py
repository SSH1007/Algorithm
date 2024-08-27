import sys
input = lambda: sys.stdin.readline().rstrip()

dp = [[[0, 0] for _ in range(101)] for _ in range(101)]
dp[1][0][0] = 1
dp[1][0][1] = 1
for k in range(100):
    for n in range(2, 101):
        dp[n][k][0] = dp[n-1][k][1] + dp[n-1][k][0]
        dp[n][k][1] = dp[n-1][k-1][1] + dp[n-1][k][0]

T = int(input())
for _ in range(T):
    N, K = map(int, input().split())
    print(dp[N][K][0] + dp[N][K][1])
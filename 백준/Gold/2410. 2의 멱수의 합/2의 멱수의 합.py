import sys
input = sys.stdin.readline
N = int(input().rstrip())
dp = [0]*(1000001)
dp[0], dp[1] = 1, 2
for n in range(2, N):
    if n%2:
        dp[n] = (dp[n-1] + dp[n//2])%1000000000
    else:
        dp[n] = dp[n-1]
print(dp[N-1])
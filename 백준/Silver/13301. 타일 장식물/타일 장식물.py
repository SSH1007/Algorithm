import sys
input = sys.stdin.readline
N = int(input().rstrip())
dp = [0]*(N+1)
dp[0], dp[1] = 1, 1
for n in range(2, N+1):
    dp[n] = dp[n-1] + dp[n-2]
print((dp[-1]+dp[-2])*2)
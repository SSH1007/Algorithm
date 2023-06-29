import sys
input = sys.stdin.readline

dp = [0, 1, 1]
n = int(input().rstrip())
i = 3
while i <= n:
    dp.append((dp[i-1] + dp[i-2])%1000000007)
    i += 1
print(dp[n])
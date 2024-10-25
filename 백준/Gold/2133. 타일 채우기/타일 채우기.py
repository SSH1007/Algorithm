import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
dp = [0]*31
dp[2], dp[4] = 3, 11
for n in range(5, N+1):
    dp[n] = dp[n-2]*4 - dp[n-4]
print(dp[N])
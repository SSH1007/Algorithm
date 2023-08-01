import sys
input = sys.stdin.readline
N = int(input().rstrip())
wine = [0]*10001
for n in range(1,N+1):
    wine[n] = int(input().rstrip())
dp = [0]*10001
dp[1] = wine[1]
dp[2] = wine[1]+wine[2]
dp[3] = max(dp[2], wine[1]+wine[3], wine[2]+wine[3])

for i in range(4, N+1):
    dp[i] = max(dp[i-1], dp[i-2]+wine[i], dp[i-3]+wine[i]+wine[i-1])
print(dp[N])
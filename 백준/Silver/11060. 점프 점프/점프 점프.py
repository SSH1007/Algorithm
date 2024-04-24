import sys
input = sys.stdin.readline
N = int(input().rstrip())
As = list(map(int, input().rstrip().split()))
dp = [1001]*N
dp[0] = 0
for i in range(N):
    for j in range(i, i+As[i]+1):
        if j < N:
            dp[j] = min(dp[i]+1, dp[j])
if dp[N-1] == 1001:
    print(-1)
else:
    print(dp[N-1])
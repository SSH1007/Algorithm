import sys
input = sys.stdin.readline
N = int(input().rstrip())
soldier = list(map(int, input().rstrip().split()))
dp = [1]*N
for i in range(1, N):
    for j in range(i):
        if soldier[j] > soldier[i]:
            dp[i] = max(dp[i], dp[j]+1)
print(N-max(dp))
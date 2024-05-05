# 마이너스로 증가하는 수열
import sys
input = sys.stdin.readline
from bisect import bisect_left
N = int(input().rstrip())
soldier = list(map(int, input().rstrip().split()))
dp = [-soldier[0]]
for i in range(1, N):
    if -soldier[i] > dp[-1]:
        dp.append(-soldier[i])
    else:
        idx = bisect_left(dp, -soldier[i])
        dp[idx] = -soldier[i]
print(N-len(dp))
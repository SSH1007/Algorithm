import sys
input = sys.stdin.readline
N = int(input().rstrip())
S = list(map(int, input().rstrip().split()))
from itertools import combinations
dp = [0]*(sum(S)+2)
for i in range(1, N+1):
    C = list(combinations(S, i))
    for c in C:
        dp[sum(c)] = 1
for i in range(1, sum(S)+2):
    if not dp[i]:
        print(i)
        break
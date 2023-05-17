import sys
input = sys.stdin.readline
K = int(input().rstrip())
dp = [0]*100
dp[0], dp[1] = 0, 1
for k in range(2, K+1):
    dp[k] = dp[k-1] + dp[k-2]
print(dp[K-1], dp[K])
# 1 B
# 2 BA
# 3 BAB
# 4 BABBA
# 5 BABBABAB
# 6 BABBABABBABBA
# 7 BABBABABBABBABABBABAB
# 0 1 1
# 1 1 2
# 1 2 3
# 2 3 5
# 3 5 6
# 5 8 13
# 8 13 21
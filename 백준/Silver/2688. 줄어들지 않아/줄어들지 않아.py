import sys
input = sys.stdin.readline


dp = [[0]*10 for _ in range(65)]
for i in range(10):
    dp[1][i] = 1

for i in range(2, 65):
    for j in range(10):
        for k in range(j, 10):
            dp[i][j] += dp[i-1][k]

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    dap = 0
    for i in range(10):
        dap += dp[n][i]
    print(dap)
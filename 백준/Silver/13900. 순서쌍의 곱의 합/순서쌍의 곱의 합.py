import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
dap = 0
dp = [0]*N
dp[0] = lst[0]
for i in range(1, N):
    dp[i] = dp[i-1]+lst[i]
for i in range(1, N):
    dap += (dp[i-1]*lst[i])
print(dap)
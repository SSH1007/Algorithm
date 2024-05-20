import sys
input = sys.stdin.readline
T = int(input().rstrip())
dp = [1, 2, 2, 4, 4]


def pp(n):
    for i in range(len(dp), n):
        dp.append(dp[i-2] + dp[(i-1)//2])


for _ in range(T):
    N = int(input().rstrip())
    if N <= len(dp):
        print(dp[N-1])
    else:
        pp(N)
        print(dp[N-1])
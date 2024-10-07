import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    M = int(input())
    dp = [[0]*(M+1) for _ in range(N+1)]
    for i in range(1, N+1):
        dp[i][i] = 1
    for n in range(1, N+1):
        for m in range(n+1, M+1):
            dp[n][m] = dp[n][m-1] + dp[n-1][m-1]
    print(dp[N][M])


if __name__ == '__main__':
    main()
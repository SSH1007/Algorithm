import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    inf = float('inf')
    dp = [[[inf]*M for _ in range(N)] for _ in range(3)]
    for i in range(3):
        dp[i][0] = maps[0]
    for n in range(1, N):
        for m in range(M):
            # \
            if m > 0:
                dp[0][n][m] = min(dp[1][n-1][m-1], dp[2][n-1][m-1]) + maps[n][m]
            # /
            if m < M-1:
                dp[2][n][m] = min(dp[0][n-1][m+1], dp[1][n-1][m+1]) + maps[n][m]
            # |
            dp[1][n][m] = min(dp[0][n-1][m], dp[2][n-1][m]) + maps[n][m]

    dap = inf
    for d in dp:
        dap = min(dap, min(d[-1]))
    print(dap)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    _ = [list(map(int, input().split())) for _ in range(n)]
    dp = [[0]*(n+1) for _ in range(n+1)]

    for i in range(n+1):
        for j in range(n+1):
            if i == 0 or j == 0:
                dp[i][j] = 1
            else:
                dp[i][j] = dp[i-1][j] + dp[i][j-1]

    print(dp[n][n], n*n)


if __name__ == '__main__':
    main()
def main():
    N = int(input())
    A = 1000000007
    dp = [[0]*(N+2) for _ in range(2)]
    dp[0][0], dp[0][1], dp[0][2] = 1, 2, 7
    for n in range(3, N+1):
        tmp = (dp[0][n-1]*2 + dp[0][n-2]*3) % A
        dp[1][n] = (dp[1][n-1] + dp[0][n-3]*2) % A
        dp[0][n] = (tmp + dp[1][n]) % A
    print(dp[0][N])


if __name__ == '__main__':
    main()
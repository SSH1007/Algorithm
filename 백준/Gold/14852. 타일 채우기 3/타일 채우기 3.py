def main():
    N = int(input())
    A = 1000000007
    dp = [[0]*3 for _ in range(2)]
    dp[0][0], dp[0][1], dp[0][2] = 1, 2, 7
    for n in range(3, N+1):
        tmp = (dp[0][(n-1) % 3]*2 + dp[0][(n-2) % 3]*3) % A
        dp[1][n % 3] = (dp[1][(n-1) % 3] + dp[0][(n-3) % 3]*2) % A
        dp[0][n % 3] = (tmp + dp[1][n % 3]) % A
    print(dp[0][N % 3])


if __name__ == '__main__':
    main()
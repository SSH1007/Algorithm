def main():
    N = int(input())
    dp = [0]*31
    dp[0], dp[2] = 1, 3
    # dp[N] = 3*dp[N-2] + (2*dp[N-4] + 2*dp[N-6] ... 2*dp[0])
    for i in range(4, N+1):
        if i % 2 == 0:
            tmp = dp[i-2]*3
            for j in range(i-2):
                tmp += dp[j]*2
            dp[i] = tmp
    print(dp[N])


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    dp = [0]*(N+1)
    dp[0] = 1
    for n in range(1, N+1):
        dp[n] = dp[n-1]
        if n-M >= 0:
            dp[n] = (dp[n-1] + dp[n-M]) % 1000000007
    print(dp[N])


if __name__ == '__main__':
    main()
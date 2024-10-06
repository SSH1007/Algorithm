import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    inf = int(1e9)
    dp = [inf]*(N+1)
    dp[0] = 0
    for coin in [1, 2, 5, 7]:
        for n in range(1, N+1):
            if n-coin >= 0:
                dp[n] = min(dp[n], dp[n-coin]+1)
    print(dp[N])


if __name__ == '__main__':
    main()
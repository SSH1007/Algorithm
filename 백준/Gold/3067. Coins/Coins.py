import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for _ in range(T):
        _ = int(input())
        coins = list(map(int, input().split()))
        M = int(input())
        dp = [0]*(M+1)
        dp[0] = 1
        for c in coins:
            for i in range(c, M+1):
                dp[i] = dp[i]+dp[i-c]
        print(dp[-1])


if __name__ == '__main__':
    main()
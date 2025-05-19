import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    dp = [0]*46
    dp[0], dp[1] = 1, 1
    for i in range(2, 46):
        dp[i] = dp[i-1] + dp[i-2]
    for _ in range(n):
        x = int(input())
        print(dp[x])


if __name__ == '__main__':
    main()
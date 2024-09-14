import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [int(input()) for _ in range(N)]
    dp = [1]*N
    for n in range(1, N):
        for i in range(n):
            if lst[i] < lst[n] and dp[n] < dp[i]+1:
                dp[n] = dp[i]+1
    print(N-max(dp))


if __name__ == '__main__':
    main()
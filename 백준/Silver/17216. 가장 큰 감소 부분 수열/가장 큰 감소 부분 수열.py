import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    # dp[i] = As[i]가 마지막인 감소 부분 수열의 합
    dp = [0]*(N+1)
    for n in range(N):
        dp[n] = As[n]
        for m in range(n):
            if As[m] > As[n]:
                dp[n] = max(dp[n], dp[m] + As[n])
    print(max(dp))


if __name__ == '__main__':
    main()
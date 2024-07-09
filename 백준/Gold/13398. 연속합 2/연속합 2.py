import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    lst = list(map(int, input().split()))
    dp = [[0]*n for _ in range(2)]
    for i in range(n):
        dp[0][0], dp[1][0] = lst[0], lst[0]
        if i == 0:
            continue
    # 수를 제거하지 않은 경우
        dp[0][i] = max(dp[0][i-1]+lst[i], lst[i])
    # 수를 하나 제거한 경우
        # 지금까지 전부 더해왔다가 i번째를 제거한 나머지 합
        # vs.
        # 이미 한번 수를 제거한 값에 i번째를 더한 합
        dp[1][i] = max(dp[0][i-1], dp[1][i-1]+lst[i])

    print(max(max(dp[0]), max(dp[1])))


if __name__ == '__main__':
    main()
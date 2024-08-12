import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    # dp[w][h] = 한 조각이 w개, 반 조각이 h개인 경우의 수
    # 약의 개수 >= 30
    dp = [[0]*31 for _ in range(31)]
    # h가 0개면 경우의 수는 1개
    for i in range(1, 31):
        dp[i][0] = 1
    for i in range(1, 31):
        for j in range(1, 31):
            if i < j:
                continue
            dp[i][j] = dp[i-1][j] + dp[i][j-1]

    while 1:
        N = int(input())
        if N == 0:
            break
        print(dp[N][N])


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = list(map(int, input().split()))
    dp = [[0]*(N+1) for _ in range(21)]
    # dp[j][i] = i번째 수까지 계산했을 때, 결과값이 j인 경우의 수
    # 0번째 수는 고정이므로 경우의 수 초기값은 1
    dp[lst[0]][0] = 1
    # 맨 마지막 수는 결과값이므로, 1번째부터 N-2번째까지를 계산한다.
    for i in range(1, N-1):
        for j in range(0, 21):
            if dp[j][i-1]:
                if 0 <= j+lst[i] <= 20:
                    dp[j+lst[i]][i] += dp[j][i-1]
                if 0 <= j-lst[i] <= 20:
                    dp[j-lst[i]][i] += dp[j][i-1]

    print(dp[lst[-1]][N-2])


if __name__ == '__main__':
    main()
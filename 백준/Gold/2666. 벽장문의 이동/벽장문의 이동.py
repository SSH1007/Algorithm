import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    a, b = map(int, input().split())
    L = int(input())
    num = []
    for _ in range(L):
        num.append(int(input()))

    # dp[i][first][second] =
    # i번째 벽장을 사용할 때 first, second 벽장이 열려있기 위한 이동 횟수

    inf = int(1e9)
    dp = [[[inf]*(N+1) for _ in range(N+1)] for _ in range(L+1)]
    # 시작할 때는 이동 횟수 0
    dp[0][a][b] = 0

    for l in range(L):
        # 사용할 벽장의 번호
        req = num[l]
        for i in range(1, N+1):
            for j in range(1, N+1):
                # 열려 있는 벽장 문은 항상 2개
                if i != j:
                    dp[l+1][req][j] = min(dp[l+1][req][j], dp[l][i][j] + abs(req-i))
                    dp[l+1][i][req] = min(dp[l+1][i][req], dp[l][i][j] + abs(req-j))
    dap = inf
    for i in range(1, N+1):
        for j in range(1, N+1):
            dap = min(dap, dp[L][i][j])
    print(dap)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    # 총 90분, 5분 간격(18개 구간). 각 간격 당 많아야 한 골 득점
    # dp[i][j][k] = i구간에 j팀이 k점을 받을 확률
    dp = [[[0]*(18+1) for _ in range(2)] for _ in range(18)]
    A = int(input())/100
    B = int(input())/100
    # 첫구간의 A, B팀의 득점, 미득점 확률(초기값)
    dp[0][0][1], dp[0][0][0] = A, 1-A
    dp[0][1][1], dp[0][1][0] = B, 1-B

    for i in range(1, 18):
        for j in range(2):
            if j == 0:
                for k in range(19):
                    dp[i][j][k] = dp[i-1][j][k-1]*A + dp[i-1][j][k]*(1-A)
            else:
                for k in range(19):
                    dp[i][j][k] = dp[i-1][j][k-1]*B + dp[i-1][j][k]*(1-B)

    # 적어도 한 팀이 골을 소수로 득점할 확률 =
    # 모든 확률 - 두 팀이 소수가 아닌 점수로 득점할 확률
    prime = [2, 3, 5, 7, 11, 13, 17]
    Ap, Bp = 0, 0
    for p in prime:
        Ap += dp[17][0][p]
        Bp += dp[17][1][p]

    dap = 1-(1-Ap)*(1-Bp)
    print(dap)


if __name__ == '__main__':
    main()
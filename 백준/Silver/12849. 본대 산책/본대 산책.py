def main():
    # 산책하는 시간 D분
    D = int(input())
    dp = [0]*8
    # D=0, 0분 동안 산책할 경우, 0에 도착하는 경우의 수는 1.
    # 따라서 dp[0]을 1로 초기화
    dp[0] = 1
    for _ in range(D):
        tmp = [0]*8
        tmp[0] = dp[1] + dp[2]
        tmp[1] = dp[0] + dp[2] + dp[3]
        tmp[2] = dp[0] + dp[1] + dp[3] + dp[4]
        tmp[3] = dp[1] + dp[2] + dp[4] + dp[5]
        tmp[4] = dp[2] + dp[3] + dp[5] + dp[6]
        tmp[5] = dp[3] + dp[4] + dp[7]
        tmp[6] = dp[4] + dp[7]
        tmp[7] = dp[5] + dp[6]
        for i in range(8):
            dp[i] = tmp[i]%1000000007
    # 출발지인 0지점에 도착하는 경우의 수는?
    print(dp[0])


if __name__ == '__main__':
    main()
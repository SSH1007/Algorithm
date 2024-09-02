import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    info = []
    for _ in range(N):
        R, G, B = map(int, input().split())
        info.append((R, G, B))
    dap = float('inf')
    for i in range(3):
        dp = [[float('inf')]*3 for _ in range(N)]
        # 1번 집 색 확정
        dp[0][i] = info[0][i]
        for j in range(1, N):
            dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + info[j][0]
            dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + info[j][1]
            dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + info[j][2]
        # 마지막 집은 1번 집과 색이 같지 않아야 된다.(선택되면 안 됨)
        dp[N-1][i] = float('inf')
        dap = min(dap, min(dp[N-1]))
    print(dap)


if __name__ == '__main__':
    main()
import sys
input = sys.stdin.readline

case = 0
while 1:
    case += 1
    N = int(input().rstrip())
    if N == 0:
        break
    graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
    cost = 0
    inf = int(1e9)
    dp = [[inf]*3 for _ in range(N)]
    dp[0][1] = graph[0][1]
    dp[0][2] = graph[0][1]+graph[0][2]
    for i in range(1, N):
        for j in range(3):
            if j == 0:
                if i == 1:
                    dp[i][0] = min(dp[i][0], graph[i][0]+dp[i-1][1])
                else:
                    dp[i][0] = min(dp[i][0], graph[i][0]+dp[i-1][0], graph[i][0]+dp[i-1][1])
            elif j == 1:
                if i == 1:
                    dp[i][1] = min(dp[i][1], graph[i][1]+dp[i-1][1], graph[i][1]+dp[i-1][2], graph[i][1]+dp[i][0])
                else:
                    dp[i][1] = min(dp[i][1], graph[i][1]+dp[i-1][0], graph[i][1]+dp[i-1][1], graph[i][1]+dp[i-1][2], graph[i][1]+dp[i][0])
            else:
                dp[i][2] = min(dp[i][2], graph[i][2]+dp[i-1][1], graph[i][2]+dp[i-1][2], graph[i][2]+dp[i][1])

    cost = dp[N-1][1]
    print(f'%d. %d' % (case, cost))
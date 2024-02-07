import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
maze = [[0]*(M+1)] + [[0]+list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[0]*(M+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, M+1):
        # 대각선으로 바로 가는 것보다 다른 곳을 경유해서 가는 것이 사탕을 더 가져갈 수 있으므로
        # 대각선으로 이동하는 케이스는 그냥 제외
        dp[i][j] = maze[i][j] + max(dp[i-1][j], dp[i][j-1])

print(dp[N][M])
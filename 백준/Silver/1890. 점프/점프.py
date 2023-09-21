N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]
dp = [[0]*N for _ in range(N)]
dp[0][0] = 1

for i in range(N):
    for j in range(N):
        if i == N-1 and j == N-1:
            print(dp[N-1][N-1])
            break
        if j+pan[i][j] < N:
            dp[i][j+pan[i][j]] += dp[i][j]
        if i+pan[i][j] < N:
            dp[i+pan[i][j]][j] += dp[i][j]
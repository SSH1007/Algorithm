N = int(input())
house = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*N for _ in range(N)] for _ in range(3)]
# dp[0] = 가로, dp[1] = 세로, dp[2] = 대각선

# 파이프가 처음부터 가로로 놓여있는 것을 감안하여 처리
dp[0][0][1] = 1
for i in range(2, N):
    if house[0][i] == 0:
        dp[0][0][i] = dp[0][0][i-1]


for r in range(1, N):
    for c in range(1, N):
        if house[r][c] == 0 and house[r-1][c] == 0 and house[r][c-1] == 0:
            dp[2][r][c] = dp[2][r-1][c-1] + dp[0][r-1][c-1] + dp[1][r-1][c-1]
        if house[r][c] == 0:
            dp[0][r][c] = dp[0][r][c-1]+dp[2][r][c-1]
            dp[1][r][c] = dp[1][r-1][c]+dp[2][r-1][c]

print(sum(list(dd[N-1][N-1] for dd in dp)))
import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[[0]*3 for _ in range(N)] for _ in range(N)]
# dp[r][c][i] = i번째 방법으로 (r, c) 지점으로 갈 수 있는 방법의 수
# (i가 0: 가로, 1: 세로, 2: 대각선)
# 파이프는 기본 가로
dp[0][1][0] = 1
# 0행은 쭉 가로로 가는 방법만 존재 -> -> ->...
for c in range(2, N):
    # 벽이 아니라면
    if maps[0][c] == 0:
        dp[0][c][0] = dp[0][c-1][0]

for r in range(1, N):
    for c in range(1, N):
        if maps[r][c] == 1:
            continue
        # 대각선 이동 가능
        if maps[r-1][c] == 0 and maps[r][c-1] == 0:
            dp[r][c][2] = dp[r-1][c-1][0] + dp[r-1][c-1][1] + dp[r-1][c-1][2]
        dp[r][c][0] = dp[r][c-1][0] + dp[r][c-1][2]
        dp[r][c][1] = dp[r-1][c][1] + dp[r-1][c][2]
print(sum(dp[N-1][N-1]))
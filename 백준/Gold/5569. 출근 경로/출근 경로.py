import sys
input = lambda: sys.stdin.readline().rstrip()

w, h = map(int, input().split())
D = 100000
dp = [[[[0]*2 for _ in range(2)] for _ in range(w)] for _ in range(h)]

# dp[h][w][a][b] = 좌표 (h,w)에 위치한 점까지 이동할 때
# a=0: 화살표 >, a=1: 화살표 V
# b=0: 안 꺾음, b=1: 꺾었음

for r in range(h):
    dp[r][0][1][0] = 1
for c in range(w):
    dp[0][c][0][0] = 1

for r in range(1, h):
    for c in range(1, w):
        dp[r][c][0][0] = (dp[r][c-1][0][0] + dp[r][c-1][0][1]) % D
        dp[r][c][0][1] = (dp[r][c-1][1][0]) % D
        dp[r][c][1][0] = (dp[r-1][c][1][0] + dp[r-1][c][1][1]) % D
        dp[r][c][1][1] = (dp[r-1][c][0][0]) % D

res = dp[h-1][w-1][0][0] + dp[h-1][w-1][0][1] + dp[h-1][w-1][1][0] + dp[h-1][w-1][1][1]
print(res % D)
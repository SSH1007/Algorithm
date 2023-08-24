N = int(input())
dp = [[0] * 10 for _ in range(N+1)]
# 힌트 : dp[x][y]는 x자리 계단 수 중, y로 끝나는 것의 개수
# 파스칼의 삼각형 비슷한 문제
mod = 1000000000

for y in range(1, 10):
    dp[1][y] = 1

for x in range(2, N+1):
    for y in range(10):
        if y == 0:
            dp[x][y] = dp[x-1][y+1] % mod
        elif y == 9:
            dp[x][y] = dp[x-1][y-1] % mod
        else:
            dp[x][y] = (dp[x-1][y-1] + dp[x-1][y+1]) % mod

print(sum(dp[N]) % mod)
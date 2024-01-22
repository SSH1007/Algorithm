N, M = map(int, input().split())
days = [0]*21
pages = [0]*301
dp = [[0]*(M+1) for _ in range(N+1)]

for m in range(1, M+1):
    day, page = map(int, input().split())
    days[m] = day
    pages[m] = page

for m in range(1, M+1):
    for n in range(1, N+1):
        if days[m] > n:
            dp[n][m] = dp[n][m-1]
        else:
            dp[n][m] = max(dp[n][m-1], pages[m]+dp[n-days[m]][m-1])

print(dp[N][M])
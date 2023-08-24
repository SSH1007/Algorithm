N = int(input())
dp = [[0]*10 for _ in range(N+1)]
for x in range(10):
    dp[1][x] = 1

for y in range(2, N+1):
    for x in range(10):
        if x == 9:
            dp[y][x] = dp[y-1][x]
        else:
            for i in range(x, 10):
                dp[y][x] += dp[y-1][i]

# for d in dp:
#     print(d)
print(sum(dp[N])%10007)
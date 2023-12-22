n = int(input())
dp = [0]*(n+1)
dp[0] = 1
for i in range(1, n+1):
    tmp = 0
    k = 0
    while k <= i-1:
        tmp += dp[0+k]*dp[i-1-k]
        k += 1
    dp[i] = tmp

print(dp[n])
K = int(input())
coins = [0, 100, 200, 500]
if K%100:
    K = K+(100-K%100)
dp = [[0]*4 for _ in range(K+1)]
for k in range(1, K+1):
    for j in range(1, 4):
        if coins[j] > k:
            dp[k][j] = dp[k][j-1]
        else:
            m = k//coins[j]
            dp[k][j] = m+dp[k-m*coins[j]][j-1]

# for i, d in enumerate(dp):
#     print(i, d)
print(dp[K][3])
n, k = map(int, input().split())
coins = []
for _ in range(n):
    coins.append(int(input()))

dp = [0] * (k+1)
dp[0] = 1

for coin in coins:
    for c in range(coin, k+1):
        if 0 <= c-coin:
            dp[c] += dp[c-coin]

print(dp[k])
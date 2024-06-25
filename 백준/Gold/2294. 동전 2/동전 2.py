n, k = map(int, input().split())
values = []
inf = int(1e9)
dp = [inf]*10001
for _ in range(n):
    v = int(input())
    if v > 10000:
        continue
    values.append(v)
    dp[v] = 1

for i in range(1, k+1):
    for v in values:
        if i-v >= 0:
            dp[i] = min(dp[i-v]+1, dp[i])

dap = dp[k]
if dap == inf:
    print(-1)
else:
    print(dp[k])
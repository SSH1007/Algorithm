n = int(input())
stair = [0 for _ in range(n)]
dp = [0 for _ in range(n)]
for i in range(n):
    a = int(input())
    stair[i] = a
dp[0] = stair[0]
if n >=2:
    dp[1] = max(stair[0] + stair[1], stair[1])
if n>= 3:
    dp[2] = max(stair[0]+stair[2], stair[1]+stair[2])
    for i in range(3,n):
        dp[i] = max(stair[i]+dp[i-2], stair[i]+stair[i-1]+dp[i-3])
print(dp[n-1])
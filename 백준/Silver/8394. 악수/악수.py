N = int(input())
dp = [0, 0, 2, 3]+[0]*N
for i in range(4, N+1):
    dp[i] = (dp[i-1]%10 + dp[i-2]%10)%10
print(dp[N])
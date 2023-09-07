N = int(input())
dp = [0]*(N+1)
dp[1] = 3
for i in range(2, N+1):
    dp[i] = dp[i-1]+i*(i+1)+((i*i+i)//2)
print(dp[N])
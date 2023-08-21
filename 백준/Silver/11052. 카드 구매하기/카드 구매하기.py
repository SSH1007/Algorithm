N = int(input())
pack = list(map(int, input().split()))
dp = [0]*(N+1)
dp[0] = pack[0]
for i in range(1, N):
    for j in range(i):
        dp[i] = max(dp[i], dp[i-j-1]+pack[j], pack[i])
print(dp[N-1])
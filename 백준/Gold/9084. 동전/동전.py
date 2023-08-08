# 예시
# coins : 2 4,  M: 8
#   0 1 2 3 4 5 6 7 8 
# 2 1 0 1 0 1 0 1 0 1
# 4 1 0 1 0 2 0 2 0 3

T = int(input())
for _ in range(T):
    N = int(input())
    coins = list(map(int, input().split()))
    M = int(input())
    dp = [0]*(M+1)
    dp[0] = 1
    for coin in coins:
        for i in range(M+1):
            if i >= coin:
                dp[i] = dp[i] + dp[i-coin]
    print(dp[M])
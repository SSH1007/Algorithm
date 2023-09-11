N = int(input())
# i장이 들어있는 카드 팩은 pack[i]원이다.
pack = list(map(int, input().split()))
# dp = N개를 갖기 위해 지불해야 하는 금액의 최솟값
dp = [10000]*N
dp[0] = pack[0]
for i in range(1, N):
    for j in range(i):
        # print(dp[i], pack[i], dp[j]+pack[i-j-1])
        dp[i] = min(dp[i], pack[i], dp[j]+pack[i-j-1])
        # print(i, j, dp)
print(dp[N-1])
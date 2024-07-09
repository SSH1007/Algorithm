n = int(input())
lst = list(map(int, input().split()))
dp = [[0]*n for _ in range(2)]
for i in range(n):
    dp[0][0], dp[1][0] = lst[0], lst[0]
    if i == 0:
        continue
# 수를 제거하지 않은 경우
    dp[0][i] = max(dp[0][i-1]+lst[i], lst[i])
# 수를 하나 제거한 경우
    dp[1][i] = max(dp[0][i-1], dp[1][i-1]+lst[i])

print(max(max(dp[0]), max(dp[1])))
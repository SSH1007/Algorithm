dp = [0]*21
dp[0] = 1
dp[1] = 1
for i in range(2, 21):
    dp[i] = dp[i-1]*i
# print(dp)

N = int(input())
cnt = 0
for i in range(21):
    if N < dp[i]:
        cnt = i - 1
        break
# print(cnt)
for i in range(cnt, -1, -1):
    if N-dp[i] >= 0:
        N -= dp[i]
    if N == 0:
        print('YES')
        break
else:
    print('NO')
import sys
input = sys.stdin.readline

# 피사노 주기 사용
# 제수 M이 10^k (k>2)일 때, 주기 P는 15*10^(k-1)
M = 1000000
k = 6
P = 15*(10**(k-1))

N = int(input().rstrip())
dp = [0, 1, 1]
i = 3
while i <= P:
    dp.append((dp[i-1] + dp[i-2])%1000000)
    i += 1
print(dp[N%P])
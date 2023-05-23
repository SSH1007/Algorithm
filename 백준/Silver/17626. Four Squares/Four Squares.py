# 1	2 3 4 5	6 7	8 9 10
# 1	2 3	1 2	3 4	2 1 2
# 자신(n)보다 같거나 작은 제곱수 i를 뺀 값 j(=> n-i)가 있다면 dp[n]에 dp[j]+1을 더하면 되는 구조
import sys
input = sys.stdin.readline
n = int(input().rstrip())
dp = [0,1]
for i in range(2, n+1):
    minCnt = 1e9
    # n에서 제곱수들을 빼가면서 dp를 갱신
    for j in range(1, int(i**0.5)+1):
        minCnt = min(minCnt, dp[i-(j**2)])
    dp.append(minCnt+1)
print(dp[n])
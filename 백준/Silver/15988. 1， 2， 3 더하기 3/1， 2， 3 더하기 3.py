import sys
input = sys.stdin.readline
T = int(input().rstrip())
lst = []
for _ in range(T):
    lst.append(int(input().rstrip()))
l = max(lst)
dp = [0, 1, 2, 4] + [0]*(l+1)
for i in range(4, l+1):
    dp[i] = (dp[i-1] + dp[i-2] + dp[i-3]) % 1000000009
for n in lst:
    print(dp[n])
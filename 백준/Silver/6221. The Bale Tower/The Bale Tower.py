import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = []
for _ in range(n):
    a, b = map(int, input().rstrip().split())
    lst.append((a, b))
lst.sort()
lst2 = [l[1] for l in lst]

dp = [1]*n
for i in range(n):
    for j in range(i):
        if lst2[i] > lst2[j]:
            dp[i] = max(dp[j]+1, dp[i])
print(max(dp))
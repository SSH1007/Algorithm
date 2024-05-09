import sys
input = sys.stdin.readline
dp = [1, 1, 3]
while 1:
    try:
        n = int(input().rstrip())
        for i in range(len(dp), n+1):
            dp.append(dp[i-1]+dp[i-2]*2)
        print(dp[n])
    except:
        break
# 2 3
# 4 11
# 6, 41
# 8, 153
# 10, 571
# 12, 2131
# 14, 7953
def solution(n):
    answer = 0
    if n%2:
        answer = 0
    else:
        dp = [0, 3, 11]
        for i in range(3, n//2+1):
            dp.append((4*dp[i-1]-dp[i-2])%1000000007)
        answer = dp[n//2]
    return answer
N = int(input())
hlst = [0] + list(map(int, input().split()))
dlst = [0] + list(map(int, input().split()))
dp = [[0]*(N+1) for _ in range(100)]
#    1번 2번 3번
# 0   0   0   0
# 1  20  20  20
# ...
# 20 20  20  20
# 21 20  30  30
# 22 20  50  50
# ...
# 79 20  50  50
# 체력 순회
for h in range(1, 100):
    # 사람순회
    for n in range(1, N+1):
        if hlst[n] > h:
            dp[h][n] = dp[h][n-1]
        else:
            dp[h][n] = max(dp[h][n-1], dp[h-hlst[n]][n-1] + dlst[n])

print(dp[99][N])
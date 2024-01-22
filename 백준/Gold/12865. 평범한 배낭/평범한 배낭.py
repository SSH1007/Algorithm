import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
weight = [0]*(100000+1)
value = [0]*(1000*100+1)
# dp는 k만큼의 무게에서 가질 수 있는 가치들의 합의 최댓값을 의미
dp = [[0]*(N+1) for _ in range(K+1)]
for n in range(1, N+1):
    W, V = map(int, input().rstrip().split())
    weight[n] = W
    value[n] = V
# 각각 k만큼의 무게 미만의 최댓값을 dp로 가져오는지 순회하며 확인
for k in range(1, K+1):
    # 1~n번째 물품까지의 dp를 체크
    for n in range(1, N+1):
        if weight[n] > k:
            dp[k][n] = dp[k][n-1]
        else:
            dp[k][n] = max(dp[k][n-1], dp[k-weight[n]][n-1]+value[n])

print(dp[K][N])
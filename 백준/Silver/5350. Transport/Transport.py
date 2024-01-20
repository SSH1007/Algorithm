P = int(input())
for _ in range(P):
    # n : 물품 수, W : 비행기 최대하중
    n, W = map(int, input().split())
    dp = [[0]*(n+1) for _ in range(W+1)]
    weight = [0]*(n+1)
    value = [0]*(n+1)
    for i in range(1, n+1):
        # w : 물품 무게, v : 물품 가치
        w, v = map(int, input().split())
        weight[i] = w
        value[i] = v
        for nn in range(1, n+1):
            for ww in range(1, W+1):
                if weight[nn] > ww:
                    dp[ww][nn] = dp[ww][nn-1]
                else:
                    dp[ww][nn] = max(dp[ww][nn-1], value[nn]+dp[ww-weight[nn]][nn-1])
    print(dp[W][n])
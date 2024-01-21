T = int(input())
for _ in range(T):
    # 너비가 2인 벽돌 100개인게 한계치이므로 dp를 201로 설정
    dp = [0]*201
    thickness = [0]*101
    width = [0]*101
    N = int(input())
    total = 0
    for n in range(1, N+1):
        t, w = map(int, input().split())
        thickness[n] = t
        width[n] = w
        # total = 최대로 늘어놓았을 때의 벽돌들의 두께 값
        total += t
    # n개씩 벽돌들을 쌓는 식으로 순회하면서
    for n in range(1, N+1):
        # total을 줄여가면서 배낭 알고리즘을 적용해간다.
        # 기존 풀어왔던 배낭 문제와는 달리 최댓값에서 빼가면서 배낭 알고리즘을 적용하는 것이 포인트.
        for i in range(total, thickness[n]+width[n]-1, -1):
            dp[i] = max(dp[i], dp[i-thickness[n]-width[n]]+thickness[n])
    print(total-dp[total])
import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
graph = []
# 표 내부 값 입력
for _ in range(N):
    lst = list(map(int, input().rstrip().split()))
    graph.append(lst)
# 구간합을 위한 dp 그래프 생성
dp = [[0]*(N+1) for _ in range(N+1)]
# dp 그래프에 구간합 입력
for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + graph[i-1][j-1]

# 입력받은 영역에 대한 구간합 출력
for _ in range(M):
    x1, y1, x2, y2 = map(int, input().rstrip().split())
    print(dp[x2][y2] + dp[x1-1][y1-1] - dp[x1-1][y2] - dp[x2][y1-1])
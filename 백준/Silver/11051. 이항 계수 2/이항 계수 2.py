# 파스칼의 삼각형 & DP
import sys
input = sys.stdin.readline

N, K = map(int, input().rstrip().split())
triangle = [[1]*(N+1) for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(1, i):
        triangle[i][j] = triangle[i-1][j-1] + triangle[i-1][j]

print(triangle[N][K] % 10007)
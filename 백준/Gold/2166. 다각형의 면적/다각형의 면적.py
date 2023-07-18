# 신발끈 공식 활용
import sys
input = sys.stdin.readline
N = int(input())
graph = [[0]*(N+2) for _ in range(4)]

for n in range(N):
    a, b = map(int, input().rstrip().split())
    graph[1][n] = a
    graph[2][n] = b

graph[1][N] = graph[1][0]
graph[2][N] = graph[2][0]

for n in range(2, N+2):
    graph[0][n] = graph[1][n-1]*graph[2][n-2]
    graph[3][n] = graph[2][n-1]*graph[1][n-2]

print(abs(sum(graph[3]) - sum(graph[0]))*0.5)
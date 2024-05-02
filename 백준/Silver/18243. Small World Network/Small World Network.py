import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
inf = float(1e9)
graph = [[inf]*N for _ in range(N)]
for _ in range(K):
    A, B = map(int, input().rstrip().split())
    graph[A-1][B-1] = 1
    graph[B-1][A-1] = 1

for k in range(N):
    for s in range(N):
        for e in range(N):
            if s == e:
                continue
            if graph[s][e] or graph[s][k]+graph[k][e]:
                graph[s][e] = min(graph[s][e], graph[s][k]+graph[k][e])

for i in range(N):
    for j in range(N):
        if graph[i][j] == inf:
            graph[i][j] = 0

# 모든 사람이 연결이 되지 않거나, 연결이 되어도 6단계를 초과하면 Big World!
for g in graph:
    # 다른 사람들과 연결 여부
    connect = sum([1 for i in g if i])
    if connect != N-1:
        print('Big World!')
        break
    level = max(g)
    if level > 6:
        print('Big World!')
        break
else:
    print('Small World!')
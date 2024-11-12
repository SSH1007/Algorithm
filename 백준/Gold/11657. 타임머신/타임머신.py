import sys
input = lambda: sys.stdin.readline().rstrip()


def BF(start):
    distance[start] = 0
    # 모든 정점에서 모든 간선을 순회한다
    for v in range(V):
        for e in range(E):
            cur, next, cost = graph[e]
            if distance[next] > distance[cur] + cost:
                distance[next] = distance[cur] + cost
                # 값 갱신을 한 시점이 V-1이다? > 사이클 성립
                if v == V-1:
                    return True
    return False


V, E = map(int, input().split())
inf = float('inf')
distance = [inf]*(V+1)
graph = []
for _ in range(E):
    graph.append(list(map(int, input().split())))

negative_cycle = BF(1)
if negative_cycle:
    print(-1)
else:
    # 1번 도시에서 다른 도시로의 시간 출력
    for i in range(2, V+1):
        if distance[i] == inf:
            print(-1)
        else:
            print(distance[i])
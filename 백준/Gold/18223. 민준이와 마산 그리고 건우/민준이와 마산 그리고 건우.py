import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


def dijkstra(start):
    distance = [inf]*(V+1)
    hq = []
    # 처음 민준이의 위치는 start
    heapq.heappush(hq, (0, start))
    distance[start] = 0
    while hq:
        dist, cur = heapq.heappop(hq)
        if dist < distance[cur]:
            continue
        for node, cost in graph[cur]:
            if distance[node] > dist + cost:
                distance[node] = dist + cost
                heapq.heappush(hq, (dist + cost, node))
    return distance[1] + distance[V]


V, E, P = map(int, input().split())
inf = float('inf')
graph = [[] for _ in range(V+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

if dijkstra(1) != dijkstra(P):
    print('GOOD BYE')
else:
    print('SAVE HIM')
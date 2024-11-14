import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq as h


def dijkstra(start):
    hq = []
    h.heappush(hq, (0, start))

    while hq:
        dist, cur = h.heappop(hq)

        if distance[cur] < dist:
            continue

        for next, cost in graph[cur]:
            if distance[next] > dist + cost:
                distance[next] = dist + cost
                h.heappush(hq, (dist + cost, next))


N, M = map(int, input().split())
As = list(map(int, input().split()))
As[-1] = 0
graph = [[] for _ in range(N)]
inf = float('inf')
distance = [inf]*N
for _ in range(M):
    a, b, t = map(int, input().split())
    if As[a] or As[b]:
        continue
    graph[a].append((b, t))
    graph[b].append((a, t))

dijkstra(0)
if distance[N-1] != inf:
    print(distance[N-1])
else:
    print(-1)
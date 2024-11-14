import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq as h


def dijkstra(start):
    hq = []
    h.heappush(hq, (0, start))
    distance[start] = 0

    while hq:
        dist, cur = h.heappop(hq)
        if distance[cur] < dist:
            continue
        for next, cost in graph[cur]:
            if distance[next] > dist + cost:
                distance[next] = dist + cost
                h.heappush(hq, (dist+cost, next))


T = int(input())
for _ in range(T):
    N, D, C = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    inf = float('inf')
    distance = [inf]*(N+1)
    for _ in range(D):
        A, B, S = map(int, input().split())
        graph[B].append((A, S))
    dijkstra(C)
    cnt, sec = 0, 0
    for i in range(1, N+1):
        if distance[i] != inf:
            cnt += 1
            if sec < distance[i]:
                sec = distance[i]
    print(cnt, sec)
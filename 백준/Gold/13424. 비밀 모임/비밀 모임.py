import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq as hq


def dijkstra():
    distance = [inf]*(N+1)
    distance[f] = 0
    q = []
    hq.heappush(q, (0, f))
    while q:
        dist, cur = hq.heappop(q)
        if dist < distance[cur]:
            continue
        for nextNode, cost in graph[cur]:
            if distance[nextNode] > cost + dist:
                distance[nextNode] = cost + dist
                hq.heappush(q, (cost + dist, nextNode))
    for n in range(N+1):
        As[n] += distance[n]
    return


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))
    As = [0]*(N+1)
    K = int(input())
    friends = list(map(int, input().split()))
    inf = float('inf')
    for f in friends:
        dijkstra()
    maxIdx, minVal = 0, inf
    for n in range(1, N+1):
        if minVal > As[n]:
            minVal = As[n]
            maxIdx = n
    print(maxIdx)
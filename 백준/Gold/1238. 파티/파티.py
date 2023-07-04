import sys
input = sys.stdin.readline
import heapq

N, M, X = map(int, input().rstrip().split())

inf = int(1e9)
distance = [inf]*(N+1)
graph = [[] for _ in range(N+1)]
dap = [[]]

for _ in range(M):
    s, e, t = map(int, input().rstrip().split())
    graph[s].append((e, t))

def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        if distance[node] < dist:
            continue
        for next in graph[node]:
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))
for i in range(1, N+1):
    dijkstra(i)
    dap.append(distance)
    distance = [inf] * (N + 1)

real_dap = 0
for n in range(1, N+1):
    if real_dap < dap[n][X] + dap[X][n]:
        real_dap = dap[n][X] + dap[X][n]
print(real_dap)
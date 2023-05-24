import sys
input = sys.stdin.readline
import heapq
N, M = map(int, input().rstrip().split())
inf = int(1e9)
distance = [inf] * (N+1)
graph = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().rstrip().split())
    # 문제에 양방향 길이라고 했으므로 a, b에 따로따로 append
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하고, 시작 노드와 함께 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, node = heapq.heappop(q)
        # 현재 가려는 node로 가는 distance에 기록된 거리가 현재 계산하려는 dist보다 이미 작다면
        # 더 가까운 경로이므로 더 이상 계산할 필요가 없다. pass
        if distance[node] < dist:
            continue
        for next in graph[node]:
            # next[1]은 위의 a,b,c 중 c(비용)에 해당된다
            cost = distance[node] + next[1]
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q, (cost, next[0]))

dijkstra(1)
print(distance[N])
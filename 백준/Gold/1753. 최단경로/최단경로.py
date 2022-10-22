import sys
input = sys.stdin.readline

# 정점의 개수 V, 간선의 개수 E
V, E = map(int, input().split())
# 시작 정점 K
K = int(input())
# 시작-끝, 가중치 정보를 담을 graph 생성
graph = [[] for _ in range(V+1)]
# 거리 배열 생성
inf = float('INF')
distance = [inf for _ in range(V+1)]
# 간선 정보를 graph에 담기
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((v,w))

import heapq
def dijkstra(start):
    q = []
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, node = heapq.heappop(q)
        
        if dist > distance[node]:
            continue
        for next in graph[node]:
            # 위의 heappush의 start에 해당되는 놈들끼리 더함
            cost = distance[node]+next[1]
            # 최단 경로와 그 경로로 가기 위한 노드를 구한다.
            if cost < distance[next[0]]:
                distance[next[0]] = cost
                heapq.heappush(q,(cost, next[0]))
        
dijkstra(K)
for d in range(1, V+1):
    print(distance[d] if distance[d]!=inf else 'INF')
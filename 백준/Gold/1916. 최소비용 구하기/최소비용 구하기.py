import heapq
import sys
input = sys.stdin.readline
# 도시 수
N = int(input().rstrip())
# 버스 수
M = int(input().rstrip())
# 간선 모음 그래프
graph = [[] for _ in range(N+1)]
# 버스 이동과 비용 입력 받기
for _ in range(M):
    s, e, c = map(int, input().rstrip().split())
    graph[s].append((e, c))
# 출발 도시와 도착 도시
start, end = map(int, input().rstrip().split())
# 거리 초기화
distance = [float('inf') for _ in range(N+1)]
# 시작점은 0으로 갱신
distance[0] = 0


def dijkstra(start):
    hq = []
    heapq.heappush(hq, (0, start))
    while hq:
        # 이동거리, 다음 이동 포인트
        interval, point = heapq.heappop(hq)
        # 만약 다음 이동 포인트까지의 거리가, hq에서 pop한 이동거리보다 짧다면?
        # 더 이상 안해도 된다. pass
        if distance[point] < interval:
            continue
        # 다음 이동 포인트에서의 갈림길(node)들을 순회
        for node in graph[point]:
            # hq에서 현재 뽑은 이동거리와 갈림길로 가는데 소요되는 비용을 합친 값이
            # 갈림길의 목적지까지의 거리보다 짧다면? 갱신
            if interval + node[1] < distance[node[0]]:
                distance[node[0]] = interval + node[1]
                # heapq에 새로운 값들 추가
                heapq.heappush(hq, (interval + node[1], node[0]))


dijkstra(start)
print(distance[end])
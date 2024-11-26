import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


N, M, t = map(int, input().split())
graph = [[] for _ in range(N+1)]
visit = set()
for _ in range(M):
    A, B, C = map(int, input().split())
    graph[A].append((B, C))
    graph[B].append((A, C))
hq = []
# 기존 점거 도시 = 1
for to, cost in graph[1]:
    heapq.heappush(hq, (cost, to))
visit.add(1)

dap, cnt = 0, 0
while len(visit) < N:
    cost, to = heapq.heappop(hq)

    # 재방문 X
    if to in visit:
        continue
    dap += (cost + cnt*t)

    for next, fee in graph[to]:
        heapq.heappush(hq, (fee, next))
    visit.add(to)
    cnt += 1
print(dap)
import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq


N = int(input())
matrix = [list(map(int, input().split())) for _ in range(N)]

hq = []
visit = set()
# (0, 0)부터 탐색하도록 하기 위해 비용 0, r=0으로 hq에 삽입
heapq.heappush(hq, (0, 0))
# 행렬 형태에선 시작점 방문은 체크하지 않는 점에 주의

dap = 0
while len(visit) < N:
    cost, r = heapq.heappop(hq)

    if r in visit:
        continue

    dap += cost
    visit.add(r)
    for c in range(N):
        # matrix[r][c]가 비용, c가 노드 역할
        if matrix[r][c] and c not in visit:
            heapq.heappush(hq, (matrix[r][c], c))
print(dap)
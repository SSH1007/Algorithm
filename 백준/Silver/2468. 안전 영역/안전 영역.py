import sys
input = sys.stdin.readline
from collections import deque
N = int(input().rstrip())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 가장 비가 많이 오는 경우를 파악
maxRain = 0
for i in range(N):
    for j in range(N):
        maxRain = max(maxRain, graph[i][j])


def BFS(x, y, visited):
    q = deque([(x, y)])
    visited[x][y] = True
    while q:
        r, c = q.popleft()
        for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < N:
                if not visited[nr][nc]:
                    visited[nr][nc] = True
                    q.append((nr, nc))



# 수위마다의 영역 개수를 담을 리스트
dap = []
# 수위만큼 루프
for r in range(maxRain):
    # 영역 개수
    cnt = 0
    # 방문 측정 리스트 초기화
    visited = [[False] * N for _ in range(N)]
    # 수위 이하의 칸은 일단 방문으로 표시(이후 방문하지 않도록)
    for i in range(N):
        for j in range(N):
            if graph[i][j] <= r:
                visited[i][j] = True

    for i in range(N):
        for j in range(N):
            if not visited[i][j]:
                BFS(i,j, visited)
                cnt += 1
    dap.append(cnt)
print(max(dap))
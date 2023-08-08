import sys
input = sys.stdin.readline
from itertools import combinations
from collections import deque
from copy import deepcopy

# 데이터 입력
N, M = map(int, input().rstrip().split())
lab = [list(map(int, input().rstrip().split())) for _ in range(N)]
answer = 0

# 벽을 세울 수 있는 빈칸의 조합 & 바이러스 리스트 만들기
empty = []
virus = []
for r in range(N):
    for c in range(M):
        if not lab[r][c]:
            empty.append((r, c))
        if lab[r][c] == 2:
            virus.append((r, c))
wall = list(combinations(empty, 3))

# delta
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]


def BFS(points):
    # 깊은 복사
    predict = deepcopy(lab)
    # 가벽 세우기
    for p in points:
        predict[p[0]][p[1]] = 1
    visited = [[0]*M for _ in range(N)]

    q = deque()
    for v in virus:
        q.append((v[0], v[1]))
    while q:
        rr, cc = q.popleft()
        visited[rr][cc] = 1
        for i in range(4):
            nr = rr + dy[i]
            nc = cc + dx[i]
            # 연구소 범위내를 이동하고
            if 0 <= nr < N and 0 <= nc < M:
                # 벽이 아닌 곳이며, 방문한 곳도 아니라면?
                if not predict[nr][nc] and not visited[nr][nc]:
                    # 다음 바이러스의 확산지로 삼는다.
                    q.append((nr, nc))
                    predict[nr][nc] = 2
                    visited[nr][nc] = 1
    dap = 0
    for p in predict:
        dap += p.count(0)
    return dap


for w in wall:
    answer = max(answer, BFS(w))
print(answer)
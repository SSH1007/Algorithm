import sys
input = sys.stdin.readline
from collections import deque
# 방의 크기 N(행)과 M(열)
N, M = map(int, input().rstrip().split())
# 시작 좌표와 방향
# d : 0 북 / 1 동 / 2 남 / 3 서
r, c, d = map(int, input().rstrip().split())
# 각 장소의 상태
# 0 : 청소되지 않음 | 1 : 벽
status = [list(map(int, input().rstrip().split())) for _ in range(N)]

# 델타 탐색 준비
dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]

# 방문 그래프 초기화
# visited = [[0]*N for _ in range(M)]


def BFS(r, c, d):
    q = deque([(r, c)])
    while q:
        rr, cc = q.popleft()
        # 현재 칸이 아직 청소되지 않은 경우, 청소
        if not status[rr][cc]:
            status[rr][cc] = 2

        # 주변 4칸 중 청소되지 않은 빈칸이 있는지 여부
        flag = False
        # 델타 탐색
        for i in range(4):
            nr = rr + dy[i]
            nc = cc + dx[i]
            # 이동한 곳이 범위 안이라면?
            if 0 <= nr < N and 0 <= nc < M:
                if status[nr][nc] == 0:
                    flag = True
                    break

        if flag:
            for _ in range(4):
                # 반시계 방향으로 90' 회전
                if d > 0:
                    d -= 1
                else:
                    d = 3
                if not status[rr+dy[d]][cc+dx[d]]:
                    q.append((rr+dy[d], cc+dx[d]))
                    break
        else:
            nr = rr + (dy[d]*-1)
            nc = cc + (dx[d]*-1)
            if 0 <= nr < N and 0 <= nc < M:
                if status[nr][nc] != 1:
                    q.append((nr, nc))
                else:
                    return

BFS(r, c, d)
dap = 0
for s in status:
    dap += s.count(2)
print(dap)
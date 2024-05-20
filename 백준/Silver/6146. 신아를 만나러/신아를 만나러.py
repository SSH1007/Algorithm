import sys
input = sys.stdin.readline
from collections import deque
X, Y, N = map(int, input().rstrip().split())
# (0, 0)이 모서리에 있는 형태가 아닌 유동적인 형태이므로
# 맵 체크, 방문체크를 딕셔너리로 처리함
pit = dict()
visited = dict()
# a, b를 N번 받으면서 상하좌우 좌표를 측정 & 구덩이 위치 추가
n_y, s_y, e_x, w_x = -500, 500, -500, 500
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    pit[(b, a)] = 1
    n_y = max(n_y, b)
    s_y = min(s_y, b)
    e_x = max(e_x, a)
    w_x = min(w_x, a)
# 델타 탐색
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
q = deque([(0, 0, 0)])
visited[(0, 0)] = 1
while q:
    r, c, cnt = q.popleft()
    if r == Y and c == X:
        print(cnt)
        break
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if s_y-1 <= nr <= n_y+1 and w_x-1 <= nc <= e_x+1:
            if not (nr, nc) in visited and not (nr, nc) in pit:
                q.append((nr, nc, cnt+1))
                visited[(nr, nc)] = 1
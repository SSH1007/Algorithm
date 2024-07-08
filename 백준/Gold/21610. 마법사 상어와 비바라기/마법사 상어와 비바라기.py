import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

# A[r][c] = (r,c)에 있는 바구니에 저장되어 있는 물의 양
dr = [0, -1, -1, -1, 0, 1, 1, 1]
dc = [-1, -1, 0, 1, 1, 1, 0, -1]


def magic(r, c):
    tmp = 0
    for y, x in [(-1, -1), (-1, 1), (1, -1), (1, 1)]:
        if 0 <= r+y < N and 0 <= c+x < N:
            if info[r+y][c+x]:
                tmp += 1
    return tmp


N, M = map(int, input().split())
info = [list(map(int, input().split())) for _ in range(N)]
# 초기 구름 위치
clouds = deque([(N-1, 0), (N-1, 1), (N-2, 0), (N-2, 1)])

for _ in range(M):
    di, si = map(int, input().split())
    visited = [[0]*N for _ in range(N)]
    moved = []
    while clouds:
        c_r, c_c = clouds.popleft()
        c_r += (dr[di-1]*si)
        c_c += (dc[di-1]*si)
        # 영역 넘어섰을 때 처리
        c_r = (c_r+N) % N
        c_c = (c_c+N) % N
        # 구름에서 비가 내려 바구니마다 1씩 증가,
        # 구름이 이동한 위치 체크, 저장
        info[c_r][c_c] += 1
        visited[c_r][c_c] = 1
        moved.append((c_r, c_c))
    # 구름이 이동한 위치에서 물복사버그 마법 시전
    for c_r, c_c in moved:
        info[c_r][c_c] += magic(c_r, c_c)

    # 5번 과정 실시
    for i in range(N):
        for j in range(N):
            if info[i][j] >= 2 and not visited[i][j]:
                clouds.append((i, j))
                info[i][j] -= 2

dap = 0
for i in info:
    dap += sum(i)
print(dap)
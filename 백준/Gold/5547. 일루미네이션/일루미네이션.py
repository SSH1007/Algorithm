import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def BFS():
    dap = 0
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        # 홀수인 경우
        if r%2:
            for i in range(6):
                nr = r + odd_dr[i]
                nc = c + odd_dc[i]
                if 0 <= nr < H+2 and 0 <= nc < W+2:
                    if not maps[nr][nc] and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                    elif maps[nr][nc]:
                        dap += 1
        # 짝수인 경우
        else:
            for i in range(6):
                nr = r + even_dr[i]
                nc = c + even_dc[i]
                if 0 <= nr < H+2 and 0 <= nc < W+2:
                    if not maps[nr][nc] and not visited[nr][nc]:
                        visited[nr][nc] = 1
                        q.append((nr, nc))
                    elif maps[nr][nc]:
                        dap += 1
    return dap


W, H = map(int, input().split())
# 지도의 바깥을 확정짓기 위해서 W+2, H+2로 데이터를 받음
tmp = [[0]+list(map(int, input().split()))+[0] for _ in range(H)]
maps = [[0]*(W+2)] + tmp + [[0]*(W+2)]
visited = [[0]*(W+2) for _ in range(H+2)]

odd_dr = [0, 0, 1, -1, -1, 1]
odd_dc = [1, -1, 0, 0, 1, 1]
even_dr = [0, 0, 1, -1, -1, 1]
even_dc = [1, -1, 0, 0, -1, -1]

print(BFS())
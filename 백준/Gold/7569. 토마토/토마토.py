import sys
input = sys.stdin.readline
from collections import deque

M, N, H = map(int, input().rstrip().split())
visited = [[[0]*M for _ in range(N)] for _ in range(H)]
boxes = [[list(map(int, input().rstrip().split())) for _ in range(N)] for _ in range(H)]
starts = []

# 이미 익은 칸(1) 체크
for h in range(H):
    for n in range(N):
        for m in range(M):
            if boxes[h][n][m] == 1:
                visited[h][n][m] = 1
                starts.append((m,n,h))

direction = [[-1,0,0],[1,0,0],[0,-1,0],[0,1,0],[0,0,1],[0,0,-1]]


def BFS(lst):
    q = deque(lst)
    while q:
        m, n, h = q.popleft()
        for dm, dn, dh in direction:
            nm = m+dm
            nn = n+dn
            nh = h+dh
            # 만약 델타탐색한 곳이 박스 범위 내이고
            if 0<=nm<M and 0<=nn<N and 0<=nh<H:
                # 빈 칸이라면
                if boxes[nh][nn][nm] == 0:
                    q.append((nm,nn,nh))
                    boxes[nh][nn][nm] = boxes[h][n][m]+1



BFS(starts)


dap = 0
for h in range(H):
    for n in range(N):
        for m in range(M):
            if boxes[h][n][m] == 0:
                print(-1)
                exit(0)
            dap = max(dap, boxes[h][n][m])
print(dap-1)
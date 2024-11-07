import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque, defaultdict


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def F():
    # visited = [[-1]*W for _ in range(H)]
    visited = defaultdict(int)

    q = deque()
    fire = []
    for h in range(H):
        for w in range(W):
            if maps[h][w] == '@':
                q.append((h, w))
                # visited[h][w] = 0
                visited[(h, w)] = 0
            elif maps[h][w] == '*':
                fire.append((h, w))
                visited[(h, w)] = -1
            else:
                visited[(h, w)] = -1

    while q:
        burn = []
        while fire:
            r, c = fire.pop()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if maps[nr][nc] == '.':
                        maps[nr][nc] = '*'
                        burn.append((nr, nc))
        fire = burn

        L = len(q)
        for _ in range(L):
            r, c = q.popleft()
            if r == 0 or c == 0 or r == H-1 or c == W-1:
                return visited[(r, c)]
                # return visited[r][c]
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if visited[(nr, nc)] == -1 and maps[nr][nc] == '.':
                    # if visited[nr][nc] == -1 and maps[nr][nc] == '.':
                        q.append((nr, nc))
                        visited[(nr, nc)] = visited[(r, c)] + 1
                        # visited[nr][nc] = visited[r][c] + 1
    return -1


T = int(input())
for _ in range(T):
    W, H = map(int, input().split())
    maps = [list(input()) for _ in range(H)]
    dap = F()
    if dap == -1:
        print('IMPOSSIBLE')
    else:
        print(dap+1)
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

N, M = map(int, input().split())
maps, lst = [], []
visited = [[[[0]*M for _ in range(N)] for _ in range(M)] for _ in range(N)]
for n in range(N):
    maps.append(input())
    for m in range(M):
        if maps[n][m] == 'o':
            lst.append(n)
            lst.append(m)

dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

q = deque()
lst.append(0)
q.append(lst)


def BFS():
    while q:
        r1, c1, r2, c2, cnt = q.popleft()
        if cnt >= 10:
            return -1
        for i in range(4):
            nr1 = r1 + dr[i]
            nc1 = c1 + dc[i]
            nr2 = r2 + dr[i]
            nc2 = c2 + dc[i]
            if 0 <= nr1 < N and 0 <= nc1 < M and 0 <= nr2 < N and 0 <= nc2 < M:
                if maps[nr1][nc1] == '#':
                    nr1 = r1
                    nc1 = c1
                if maps[nr2][nc2] == '#':
                    nr2 = r2
                    nc2 = c2
                if not visited[nr1][nc1][nr2][nc2]:
                    q.append((nr1, nc1, nr2, nc2, cnt+1))
                    visited[nr1][nc1][nr2][nc2] = 1
            elif 0 <= nr1 < N and 0 <= nc1 < M:
                return cnt + 1
            elif 0 <= nr2 < N and 0 <= nc2 < M:
                return cnt + 1
            else:
                continue
    return -1


print(BFS())
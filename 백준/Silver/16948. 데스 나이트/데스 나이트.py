from collections import deque
dkr = [-2, -2, 0, 0, 2, 2]
dkc = [-1, 1, -2, 2, -1, 1]


def bfs(r1, c1):
    q = deque([(r1, c1)])
    visited[r1][c1] = True
    while q:
        pdkr, pdkc = q.popleft()
        for i in range(6):
            ndkr = pdkr+dkr[i]
            ndkc = pdkc+dkc[i]
            if 0<=ndkr<N and 0<=ndkc<N:
                if not visited[ndkr][ndkc]:
                    q.append((ndkr, ndkc))
                    visited[ndkr][ndkc] = True
                    pan[ndkr][ndkc] = pan[pdkr][pdkc] + 1


N = int(input())
pan = [[0]*N for _ in range(N)]
visited = [[False]*N for _ in range(N)]
r1, c1, r2, c2 = map(int, input().split())
bfs(r1, c1)
if pan[r2][c2]:
    print(pan[r2][c2])
else:
    print(-1)
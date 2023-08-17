import sys
input = sys.stdin.readline
from collections import deque
T = int(input().rstrip())

dr = [-2,-2,-1,1,2,2,1,-1]
dc = [-1,1,2,2,1,-1,-2,-2]

for _ in range(T):
    I = int(input().rstrip())
    start = list(map(int, input().rstrip().split()))
    end = list(map(int, input().rstrip().split()))
    visited = [[0]*I for _ in range(I)]
    q = deque([start])
    # visited[start[0]][start[1]] = 1
    while q:
        r, c = q.popleft()
        if r == end[0] and c == end[1]:
            break
        for i in range(8):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < I and 0 <= nc < I:
                if not visited[nr][nc]:
                    visited[nr][nc] = visited[r][c] + 1
                    q.append((nr, nc))
    # for v in visited:
    #     print(v)
    print(visited[end[0]][end[1]])
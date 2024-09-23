import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def main():
    R, C = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(R)]
    dap = 0
    q = deque([(0, 0)])
    visited = [[0]*C for _ in range(R)]
    visited[0][0] = 1
    while sum([sum(m) for m in maps]) != 0:
        next_q = []
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    if not visited[nr][nc]:
                        if maps[nr][nc] != 0:
                            maps[nr][nc] += 1
                            if maps[nr][nc] >= 3:
                                next_q.append((nr, nc))
                                visited[nr][nc] = 1
                                maps[nr][nc] = 0
                        else:
                            q.append((nr, nc))
                            visited[nr][nc] = 1
        q = deque(next_q)
        dap += 1
    print(dap)


if __name__ == '__main__':
    main()
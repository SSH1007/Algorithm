import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    N = int(input())
    maps = [list(map(int, list(input()))) for _ in range(N)]
    # visited는 방문과 방을 바꾼 횟수를 모두 의미
    # -1 : 미방문, n : 방문, 방을 바꾼 횟수
    visited = [[-1]*N for _ in range(N)]
    # 흰 방에서 출발
    visited[0][0] = 0
    q = deque([(0, 0)])
    while q:
        r, c = q.popleft()
        if r == N-1 and c == N-1:
            print(visited[r][c])
            break
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < N:
                if visited[nr][nc] == -1:
                    if maps[nr][nc] == 0:
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))
                    else:
                        visited[nr][nc] = visited[r][c]
                        q.appendleft((nr, nc))


if __name__ == '__main__':
    main()
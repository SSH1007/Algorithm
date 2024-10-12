import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def main():
    N, M = map(int, input().split())
    r1, c1, r2, c2 = map(int, input().split())
    room = [list(input()) for _ in range(N)]
    # '0'은 0초만에 이동할 수 있다고 생각해라
    time = [[-1]*M for _ in range(N)]
    time[r1-1][c1-1] = 0
    q = deque([(r1-1, c1-1)])
    while q:
        r, c = q.popleft()
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if time[nr][nc] == -1:
                    if room[nr][nc] == '0':
                        time[nr][nc] = time[r][c]
                        # '0'인 부분을 우선해서 체크해야 함
                        q.appendleft((nr, nc))
                    else:
                        time[nr][nc] = time[r][c] + 1
                        q.append((nr, nc))
    print(time[r2-1][c2-1])


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

# 동서남북
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


def main():
    # 쥐 둥지, 치즈공장, 방해물, 빈 공간
    # 쥐는 둥지에서 출발해서 모든 치즈공장을 들러서 치즈를 하나씩 먹는다
    # N개의 치즈공장이 있고, 치즈 종류는 1종뿐이다.
    # 치즈의 단단함은 공장마다 달라서, 공장마다 1~N 정도로 단단한 치즈를 생산한다.
    # 쥐의 체력은 1부터 시작해, 치즈를 하나 먹는 걸로 체력이 1 늘어난다.
    # 자신의 체력보다 단단한 치즈는 먹지 못한다.
    # 동서남북 옆에 있는 구역으로 1분 걸려 이동이 가능. 방해물이 있는 곳은 갈 수 없다.
    # 치즈 공장을 그냥 지나치는 것도 가능하다.
    # 모든 치즈를 먹을 때까지 걸리는 최단 시간을 구하라
    H, W, N = map(int, input().split())
    maps = [list(input()) for _ in range(H)]
    visited = [[-1]*W for _ in range(H)]

    q = deque()
    for r in range(H):
        for c in range(W):
            if maps[r][c] == 'S':
                q.append((r, c))
                visited[r][c] = 0

    dap = 0
    for size in range(1, N+1):
        while q:
            r, c = q.popleft()
            if maps[r][c] == str(size):
                dap += visited[r][c]
                q = deque([(r, c)])
                break
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < H and 0 <= nc < W:
                    if visited[nr][nc] == -1 and maps[nr][nc] != 'X':
                        visited[nr][nc] = visited[r][c] + 1
                        q.append((nr, nc))

        visited = [[-1]*W for _ in range(H)]
        visited[q[0][0]][q[0][1]] = 0
    print(dap)


if __name__ == '__main__':
    main()
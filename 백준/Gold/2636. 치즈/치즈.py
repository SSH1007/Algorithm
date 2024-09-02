import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]


def main():
    R, C = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(R)]
    cheese = [sum(sum(m) for m in maps)]

    # 합이 0보다 클 때까지 무한 반복
    while sum(sum(m) for m in maps) > 0:
        visited = [[0]*C for _ in range(R)]
        q = deque([(0, 0)])
        visited[0][0] = 1
        melt = set()
        # BFS 탐색, 1이 나오면 체크
        while q:
            r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    if not visited[nr][nc]:
                        if maps[nr][nc] == 1:
                            melt.add((nr, nc))
                        else:
                            q.append((nr, nc))
                        visited[nr][nc] = 1
        for r, c in list(melt):
            maps[r][c] = 0
        cheese.append(sum(sum(m) for m in maps))
    print(len(cheese)-1)
    print(cheese[-2])


if __name__ == '__main__':
    main()
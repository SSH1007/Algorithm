import sys
input = sys.stdin.readline
from collections import deque
# 세로 크기 N, 가로 크기 M
N, M = map(int, input().rstrip().split())
# 비트마스킹으로 a~f까지의 열쇠 확인
key_check = [[[0]*(1 << 6) for _ in range(M)] for _ in range(N)]
maze = [list(input().rstrip()) for _ in range(N)]

# 민식이 현재 위치 찾고 그 위치 빈칸으로 수정
startR, startC = 0, 0
for n in range(N):
    for m in range(M):
        if maze[n][m] == '0':
            startR, startC = n, m
            maze[n][m] = '.'

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]

q = deque([(startR, startC, 0)])
key_check[startR][startC][0] = 1


def BFS():
    while q:
        r, c, key = q.popleft()
        if maze[r][c] == '1':
            print(key_check[r][c][key] - 1)
            return
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < N and 0 <= nc < M:
                if not key_check[nr][nc][key] and maze[nr][nc] != '#':
                    if maze[nr][nc].islower():
                        tmp_key = key | (1 << (ord(maze[nr][nc])-ord('a')))
                        key_check[nr][nc][tmp_key] = key_check[r][c][key] + 1
                        q.append((nr, nc, tmp_key))
                    elif maze[nr][nc].isupper():
                        if key & (1 << (ord(maze[nr][nc])-ord('A'))):
                            key_check[nr][nc][key] = key_check[r][c][key] + 1
                            q.append((nr, nc, key))
                    else:
                        key_check[nr][nc][key] = key_check[r][c][key] + 1
                        q.append((nr, nc, key))
    print(-1)


BFS()
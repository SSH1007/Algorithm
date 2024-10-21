import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque


def main():
    inf = float('inf')
    R, C = map(int, input().split())
    # .: 빈 곳, *: 물, X: 바위
    # D: 비버, S: 고슴도치

    dr = [1, -1, 0, 0]
    dc = [0, 0, 1, -1]

    # 고슴도치: 델타탐색(이동), 물: 델타탐색(확장)
    # 바위는 아무도 못 지나감.
    # 고슴도치는 물 속으로 못 가고, 물은 비버의 소굴로 갈 수 없음
    # 고슴도치는 물이 찰 예정인 칸으로 이동할 수 없다!

    maps = [list(input()) for _ in range(R)]
    visited = [[-1]*C for _ in range(R)]
    # 짐승 좌표 초기화
    D, S = [0, 0], [0, 0]
    # 물 좌표들은 해시에 기록
    water = dict()
    for r in range(R):
        for c in range(C):
            if maps[r][c] == 'D':
                D = [r, c]
            elif maps[r][c] == 'S':
                S = [r, c]
            elif maps[r][c] == '*':
                water[(r, c)] = 1

    visited[S[0]][S[1]] = 0
    q = deque([(S)])
    while q:
        flood = dict()
        for w in water:
            w_r, w_c = w[0], w[1]
            for i in range(4):
                w_nr = w_r + dr[i]
                w_nc = w_c + dc[i]
                if 0 <= w_nr < R and 0 <= w_nc < C:
                    if maps[w_nr][w_nc] == '.':
                        maps[w_nr][w_nc] = '*'
                        flood[(w_nr, w_nc)] = 1
        water = flood
        
        L = len(q)
        for _ in range(L):
            r, c = q.popleft()
            for i in range(4):
                nr = r + dr[i]
                nc = c + dc[i]
                if 0 <= nr < R and 0 <= nc < C:
                    if maps[nr][nc] == '.' or maps[nr][nc] == 'D':
                        if visited[nr][nc] == -1:
                            q.append((nr, nc))
                            visited[nr][nc] = visited[r][c] + 1

    if visited[D[0]][D[1]] == -1:
        print('KAKTUS')
    else:
        print(visited[D[0]][D[1]])

if __name__ == '__main__':
    main()
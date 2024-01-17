import sys
input = sys.stdin.readline
from collections import deque
R, C = map(int, input().rstrip().split())
lake = [list(input().rstrip()) for _ in range(R)]
swan_check = [[0]*C for _ in range(R)]
melting_check = [[0]*C for _ in range(R)]
today_water, today_swan, next_water, next_swan = deque(), deque(), deque(), deque()

# 시작점과 끝점 찾기 & BFS 돌릴 지점들 탐색
endx, endy = 0, 0
for r in range(R):
    for c in range(C):
        # 백조가 있을 때
        if lake[r][c] == 'L':
            if today_swan:  # 이미 알고 있는 백조 위치가 있다면 이것이 두번째 백조
                endy, endx = r, c
            else:
                today_swan.append((r, c))
                swan_check[r][c] = 1
            # 백조가 있던 곳도 그냥 물에 속한다는 것에 주의
            lake[r][c] = '.'
            today_water.append((r, c))
            melting_check[r][c] = 1
        # 그냥 물일 때
        elif lake[r][c] == '.':
            today_water.append((r, c))
            melting_check[r][c] = 1

dr = [-1, 1, 0, 0]
dc = [0, 0, -1, 1]


# 얼음이 녹는 BFS
def meltingBFS():
    while today_water:
        r, c = today_water.popleft()
        lake[r][c] = '.'
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if not melting_check[nr][nc]:
                    if lake[nr][nc] == 'X':
                        next_water.append((nr, nc))
                    else:
                        today_water.append((nr, nc))
                    melting_check[nr][nc] = 1
    return


# 백조가 이동하는 BFS
def swanBFS():
    while today_swan:
        r, c = today_swan.popleft()
        if r == endy and c == endx:
            return True
        for i in range(4):
            nr = r + dr[i]
            nc = c + dc[i]
            if 0 <= nr < R and 0 <= nc < C:
                if not swan_check[nr][nc]:
                    if lake[nr][nc] == '.':
                        today_swan.append((nr, nc))
                    else:
                        next_swan.append((nr, nc))
                    swan_check[nr][nc] = 1
    return False


day = 0
while 1:
    meltingBFS()
    if swanBFS():
        break
    day += 1
    today_swan = next_swan
    today_water = next_water
    next_swan = deque()
    next_water = deque()

print(day)
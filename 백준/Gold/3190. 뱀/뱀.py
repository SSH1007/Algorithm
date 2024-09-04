import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque, defaultdict


def main():
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]

    # 맵 크기, 뱀 위치, 몸통, 방향 초기화
    N = int(input())
    r, c = 0, 0
    snake = deque([(r, c)])
    way = 0

    # 사과 위치 표시
    K = int(input())
    maps = [[0]*N for _ in range(N)]
    apples = [list(map(int, input().split())) for _ in range(K)]
    for y, x in apples:
        maps[y-1][x-1] = 1

    # 방향 변경 시간 기록
    L = int(input())
    move = defaultdict(str)
    for _ in range(L):
        X, C = input().split()
        X = int(X)
        move[X] = C

    t = 1
    while 1:
        r += dr[way]
        c += dc[way]

        # 벽 충돌
        if 0 > r or N <= r or 0 > c or N <= c:
            print(t)
            exit(0)
        # 자기자신 충돌
        if (r, c) in snake:
            print(t)
            exit(0)
        # 사과가 있으면 사과를 먹는다
        if maps[r][c] == 1:
            maps[r][c] = 0
        # 없으면 꼬리칸을 비워준다
        else:
            snake.pop()
        # 이동한 칸에 머리가 위치
        snake.appendleft((r, c))

        # 방향 전환
        if move[t] == 'D':
            way -= 1
            if way < 0:
                way = 3
        elif move[t] == 'L':
            way += 1
            way %= 4
        t += 1


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque, defaultdict


def main():
    dr = [0, -1, 0, 1]
    dc = [1, 0, -1, 0]
    N = int(input())
    maps = [[0]*N for _ in range(N)]
    maps[0][0] = 1
    way = 0
    snake = deque([(0, 0)])
    K = int(input())
    apples = [list(map(int, input().split())) for _ in range(K)]
    for r, c in apples:
        maps[r-1][c-1] = 2
    L = int(input())
    move = defaultdict(str)
    for _ in range(L):
        X, C = input().split()
        X = int(X)
        move[X] = C
    t = 1
    while 1:
        head = snake[0]
        r, c = head
        tail = snake.pop()
        nr = r + dr[way]
        nc = c + dc[way]
        if 0 > nr or N <= nr or 0 > nc or N <= nc:
            print(t)
            exit(0)
        if maps[nr][nc] == 1:
            print(t)
            exit(0)
        if maps[nr][nc] == 2:
            maps[tail[0]][tail[1]] = 1
            snake.append((tail[0], tail[1]))
        else:
            maps[tail[0]][tail[1]] = 0
        maps[nr][nc] = 1
        snake.appendleft((nr, nc))
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
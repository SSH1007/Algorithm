import sys
input = sys.stdin.readline
R, C, N = map(int, input().rstrip().split())
pan = [list(input().rstrip()) for _ in range(R)]
bomb = [['O']*C for _ in range(R)]
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]


def boom(info):
    real = [['O']*C for _ in range(R)]
    for r in range(R):
        for c in range(C):
            if info[r][c] == 'O':
                real[r][c] = '.'
                for i in range(4):
                    nr = r + dr[i]
                    nc = c + dc[i]
                    if 0 <= nr < R and 0 <= nc < C:
                        real[nr][nc] = '.'
    return real


# 반복 테스트해본 결과, 4 단위로 사이클이 존재
if N == 1:
    for p in pan:
        print(''.join(p))
elif N % 2 == 0:
    for b in bomb:
        print(''.join(b))
else:
    bomb3 = boom(pan)
    bomb1 = boom(bomb3)

    if N % 4 == 3:
        for b in bomb3:
            print(''.join(b))
    elif N % 4 == 1:
        for b in bomb1:
            print(''.join(b))
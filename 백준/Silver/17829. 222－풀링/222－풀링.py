import sys
input = sys.stdin.readline
N = int(input().rstrip())
pan = [list(map(int, input().rstrip().split())) for _ in range(N)]


def f(r, c, size):
    if size == 2:
        tmp = [0]*4
        cnt = 0
        for i in range(r, r+2):
            for j in range(c, c+2):
               tmp[cnt] = pan[i][j]
               cnt += 1
        tmp.sort()
        return tmp[2]
    else:
        tmp = [0]*4
        size //= 2
        tmp[0] = f(r, c, size)
        tmp[1] = f(r, c+size, size)
        tmp[2] = f(r+size, c, size)
        tmp[3] = f(r+size, c+size, size)
        tmp.sort()
        return tmp[2]


print(f(0, 0, N))
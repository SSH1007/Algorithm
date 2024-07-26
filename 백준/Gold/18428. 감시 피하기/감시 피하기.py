import sys
input = lambda: sys.stdin.readline().rstrip()
from itertools import combinations


def main():
    N = int(input())
    maps = [list(input().split()) for _ in range(N)]
    teacher = []
    lst = []
    for i in range(N):
        for j in range(N):
            if maps[i][j] == 'X':
                lst.append((i, j))
            elif maps[i][j] == 'T':
                teacher.append((i, j))

    comb = list(combinations(lst, 3))

    def F(t):
        tmp = 0
        r, c = t[0], t[1]
        while r < N-1:
            r += 1
            if maps[r][c] == 'O':
                tmp += 1
                break
            elif maps[r][c] == 'S':
                break
        else:
            tmp += 1
            
        r, c = t[0], t[1]
        while r > 0:
            r -= 1
            if maps[r][c] == 'O':
                tmp += 1
                break
            elif maps[r][c] == 'S':
                break
        else:
            tmp += 1
            
        r, c = t[0], t[1]
        while c < N-1:
            c += 1
            if maps[r][c] == 'O':
                tmp += 1
                break
            elif maps[r][c] == 'S':
                break
        else:
            tmp += 1
            
        r, c = t[0], t[1]
        while c > 0:
            c -= 1
            if maps[r][c] == 'O':
                tmp += 1
                break
            elif maps[r][c] == 'S':
                break
        else:
            tmp += 1

        if tmp == 4:
            return 1
        else:
            return 0

    for obstacle in comb:
        tmp = 0
        for o_r, o_c in obstacle:
            maps[o_r][o_c] = 'O'
        for t in teacher:
            tmp += F(t)
        if tmp == len(teacher):
            print('YES')
            return
        for o_r, o_c in obstacle:
            maps[o_r][o_c] = 'X'
    print('NO')


if __name__ == '__main__':
    main()
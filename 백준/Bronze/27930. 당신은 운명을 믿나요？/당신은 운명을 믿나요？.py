import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    k, y = 0, 0
    for s in S:
        if k == 0 and s == 'K':
            k += 1
        elif k == 1 and s == 'O':
            k += 1
        elif k == 2 and s == 'R':
            k += 1
        elif k == 3 and s == 'E':
            k += 1
        elif k == 4 and s == 'A':
            print('KOREA')
            return
        if y == 0 and s == 'Y':
            y += 1
        elif y == 1 and s == 'O':
            y += 1
        elif y == 2 and s == 'N':
            y += 1
        elif y == 3 and s == 'S':
            y += 1
        elif y == 4 and s == 'E':
            y += 1
        elif y == 5 and s == 'I':
            print('YONSEI')
            return


if __name__ == '__main__':
    main()
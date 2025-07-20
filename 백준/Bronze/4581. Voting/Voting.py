import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        S = input()
        if S == '#':
            break
        y, n, a = 0, 0, 0
        for s in S:
            if s == 'Y':
                y += 1
            elif s == 'N':
                n += 1
            elif s == 'A':
                a += 1
        if a >= len(S)/2:
            print('need quorum')
        elif y > n:
            print('yes')
        elif y < n:
            print('no')
        else:
            print('tie')


if __name__ == '__main__':
    main()
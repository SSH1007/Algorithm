import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        S = list(input().split())
        sj = ''.join(S)
        if sj == 'END':
            break
        s = set(sj)
        if len(sj) == len(s):
            print(' '.join(S))


if __name__ == '__main__':
    main()
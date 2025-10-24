import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        C, W, L, P = map(int, input().split())
        if C+W+L+P == 0:
            break
        print(((C**W)**L)**P)


if __name__ == '__main__':
    main()
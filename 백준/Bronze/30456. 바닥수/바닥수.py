import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, L = map(int, input().split())
    print('1'*(L-1), N, sep='')


if __name__ == '__main__':
    main()
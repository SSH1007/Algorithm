import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    a, b = map(int, input().split())
    print('O' if a/0.5*6%360==b else 'X')


if __name__ == '__main__':
    main()
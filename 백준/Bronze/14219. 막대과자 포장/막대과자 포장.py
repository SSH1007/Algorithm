import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    if n%3==0 or m%3==0:
        print('YES')
    else:
        print('NO')


if __name__ == '__main__':
    main()
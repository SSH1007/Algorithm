import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    s = set(int(input()) for _ in range(N))
    print('NO' if len(s) == 5 else 'YES')


if __name__ == '__main__':
    main()
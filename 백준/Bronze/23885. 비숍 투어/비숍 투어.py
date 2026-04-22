import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    sx, sy = map(int, input().split())
    ex, ey = map(int, input().split())
    if N == 1 or M == 1:
        print('YES' if (sx, sy) == (ex, ey) else 'NO')
    else:
        print('YES' if (sx+sy)%2 == (ex+ey)%2 else 'NO')


if __name__ == '__main__':
    main()
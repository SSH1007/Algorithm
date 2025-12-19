import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    ix, iy, ax, ay = 100, 100, 1, 1
    for _ in range(N):
        X, Y = map(int, input().split())
        ix = min(ix, X)
        iy = min(iy, Y)
        ax = max(ax, X)
        ay = max(ay, Y)
    print(max(ax-ix, ay-iy)**2)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    ax, ay, ix, iy = -10, -10, 10, 10
    for _ in range(int(input())):
        a, b, c, d = map(int, input().split())
        ax = max(ax, c)
        ay = max(ay, d)
        ix = min(ix, a)
        iy = min(iy, b)
        print(((ax-ix)+(ay-iy))*2)


if __name__ == '__main__':
    main()
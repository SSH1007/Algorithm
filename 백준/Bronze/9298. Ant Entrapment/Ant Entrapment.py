import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    for t in range(1, T+1):
        N = int(input())
        nx, ny, xx, xy = 1000, 1000, -1000, -1000
        for _ in range(N):
            x, y = map(float, input().split())
            nx = min(nx, x)
            ny = min(ny, y)
            xx = max(xx, x)
            xy = max(xy, y)
        print(f'Case {t}: Area {(xx-nx)*(xy-ny)}, Perimeter {(xx-nx)*2+(xy-ny)*2}')


if __name__ == '__main__':
    main()
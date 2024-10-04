import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    maps = [list(map(int, input().split())) for _ in range(N)]
    haps = [[0]*(M+1) for _ in range(N+1)]
    for n in range(1, N+1):
        for m in range(1, M+1):
            haps[n][m] = maps[n-1][m-1] + haps[n-1][m] + haps[n][m-1] - haps[n-1][m-1]
    for _ in range(int(input())):
        x1, y1, x2, y2 = map(int, input().split())
        print(haps[x2][y2]-haps[x1-1][y2]-haps[x2][y1-1]+haps[x1-1][y1-1])


if __name__ == '__main__':
    main()
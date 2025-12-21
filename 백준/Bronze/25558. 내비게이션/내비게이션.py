import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    sx, sy, ex, ey = map(int, input().split())
    dap, R = 0, float('inf')
    for n in range(1, N+1):
        M, tmp = int(input()), 0
        tsx, tsy = sx, sy
        for _ in range(M):
            mx, my = map(int, input().split())
            tmp += abs(tsx-mx) + abs(tsy-my)
            tsx, tsy = mx, my
        tmp += abs(tsx-ex) + abs(tsy-ey)
        if tmp < R:
            dap = n
            R = tmp
    print(dap)


if __name__ == '__main__':
    main()
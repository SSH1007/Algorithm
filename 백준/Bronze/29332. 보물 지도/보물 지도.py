import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    inf = float('inf')
    u, d, r, l = inf, -inf, inf, -inf
    N = int(input())
    for _ in range(N):
        x, y, dr = input().split()
        x, y = int(x), int(y)
        if dr == 'U':
            d = max(d, y+1)
        elif dr == 'D':
            u = min(u, y-1)
        elif dr == 'R':
            l = max(l, x+1)
        else:
            r = min(r, x-1)
    if inf in [u, d, r, l] or -inf in [u, d, r, l]:
        print('Infinity')
    else:
        print((u-d+1)*(r-l+1))


if __name__ == '__main__':
    main()
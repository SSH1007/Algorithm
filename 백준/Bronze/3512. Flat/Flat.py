import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, c = map(int, input().split())
    tar, tab, cf, bal = 0, 0, 0, 0
    for _ in range(n):
        a, t = input().split()
        a = int(a)
        tar += a
        if t == 'bedroom':
            tab += a
        if t == 'balcony':
            bal += a
        cf += a
    print(tar)
    print(tab)
    print(cf*c-bal/2*c)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    dap = 0
    fl, fr = 0, 0
    for _ in range(T):
        l, r = map(int, input().split())
        if fl == l and l != 0:
            dap += 1
        if fr == r and r != 0:
            dap += 1
        if r != 0 and l == r:
            dap += 1
        fl = l
        fr = r
    print(dap)


if __name__ == '__main__':
    main()
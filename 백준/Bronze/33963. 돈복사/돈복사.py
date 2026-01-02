import sys
input = lambda: sys.stdin.readline().rstrip()


def f(N):
    d = 0
    while N > 0:
        N //= 10
        d += 1
    return d


def main():
    dap = 0
    N = int(input())
    while 1:
        M = N*2
        if f(M) > f(N):
            break
        dap += 1
        N = M
    print(dap)


if __name__ == '__main__':
    main()
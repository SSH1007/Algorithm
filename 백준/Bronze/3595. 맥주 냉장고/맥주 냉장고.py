import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = float('inf')
    a, b, c = 0, 0, 0
    for n in range(1, N+1):
        if N%n == 0:
            for m in range(1, N//n+1):
                if (N//n) % m == 0:
                    o = N//n//m
                    if dap > 2*(n*m+m*o+n*o):
                        dap = 2*(n*m+m*o+n*o)
                        a, b, c = n, m, o
    print(a, b, c)


if __name__ == '__main__':
    main()
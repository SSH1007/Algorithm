import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = input()
    L = len(N)
    N = int(N)
    dap = 0
    for _ in range(L):
        a = N%10
        b = N//10
        N = b+a*(10**(L-1))
        dap += b+a*(10**(L-1))
    print(dap)


if __name__ == '__main__':
    main()
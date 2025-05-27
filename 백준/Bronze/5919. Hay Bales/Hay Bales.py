import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = list(int(input()) for _ in range(N))
    eq = sum(lst)//N
    dap = 0
    for l in lst:
        if l > eq:
            dap += l-eq
    print(dap)


if __name__ == '__main__':
    main()
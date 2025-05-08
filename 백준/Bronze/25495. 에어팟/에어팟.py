import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap, A, tmp = 0, 0, 0
    lst = list(map(int, input().split()))
    for n in range(N):
        if A == lst[n]:
            tmp *= 2
            dap += tmp
        else:
            tmp = 2
            dap += tmp
            A = lst[n]
        if dap >= 100:
            dap = 0
            A = 0
    print(dap)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    N = list(input().split())
    dap = N[0][0]
    for i in range(1, n):
        if len(N[i-1]) > len(N[i]):
            dap += ' '
        else:
            dap += N[i][len(N[i-1])-1]
    print(dap)


if __name__ == '__main__':
    main()
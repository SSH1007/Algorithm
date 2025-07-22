import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, k, T = map(int, input().split())
    lst = list(map(int, input().split()))
    dap = 0
    for i in range(n):
        if T > k:
            tmp = T+lst[i]-abs(T-k)
        else:
            tmp = T+lst[i]+abs(T-k)
        T = tmp
        dap += (T-k)
    print(dap)


if __name__ == '__main__':
    main()
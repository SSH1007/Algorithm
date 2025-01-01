import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m = map(int, input().split())
    Ts = list(map(int, input().split()))
    dap = tmp = sum(Ts[:m])
    for i in range(m, n):
        tmp += Ts[i]
        tmp -= Ts[i-m]
        if dap < tmp:
            dap = tmp
    print(dap)


if __name__ == '__main__':
    main()
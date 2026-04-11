import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    As = list(map(int, input().split()))
    dap = 0
    for n in range(1, N):
        if As[n-1] < As[n]:
            continue
        elif As[n] <= As[n-1] < As[n]+K:
            As[n] += K
            dap += 1
        else:
            print(-1)
            exit(0)
    print(dap)


if __name__ == '__main__':
    main()
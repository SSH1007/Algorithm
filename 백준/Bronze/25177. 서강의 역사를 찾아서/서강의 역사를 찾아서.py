import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    As += [0]*abs(N-M)
    dap = 0
    for i in range(M):
        if As[i] < Bs[i]:
            dap = max(dap, Bs[i]-As[i])
    print(dap)


if __name__ == '__main__':
    main()
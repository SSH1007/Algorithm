import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    dap = 0
    for n in range(N):
        if As[n] <= Bs[n]:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()
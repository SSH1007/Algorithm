import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    Ns = sorted(list(map(int, input().split())))
    dap = 0
    for k in range(1, K+1):
        dap += Ns[-k]-k+1
    print(dap)


if __name__ == '__main__':
    main()
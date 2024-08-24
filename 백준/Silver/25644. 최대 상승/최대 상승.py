import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    As = list(map(int, input().split()))
    dap, minV = 0, As[0]
    for i in range(N):
        dap = max(dap, As[i]-minV)
        minV = min(minV, As[i])
    print(dap)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def graph1(X, Y, x):
    return Y/X*x


def graph2(X, Y, x):
    return -Y/X*x+Y


def main():
    W, H, N = map(int, input().split())
    dap = 0.0
    for i in range(1, N):
        x, y = graph1(W, H, i*W/N), graph2(W, H, i*W/N)
        dap += abs(x-y)
    print(dap)


if __name__ == '__main__':
    main()
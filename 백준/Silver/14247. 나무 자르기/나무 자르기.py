import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dap = 0
    N = int(input())
    dap += sum(list(map(int, input().split())))
    grow = sorted(list(map(int, input().split())))
    for i in range(1, N):
        dap += grow[i]*i
    print(dap)


if __name__ == '__main__':
    main()
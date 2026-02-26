import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = 1
    for i in range(1, N+1):
        dap *= i
    print(dap)


if __name__ == '__main__':
    main()
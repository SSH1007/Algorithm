import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = 0
    s = int(input())
    for _ in range(N-1):
        x = int(input())
        dap += (x-s)**2
        s = x
    print(dap)


if __name__ == '__main__':
    main()
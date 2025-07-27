import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    X = int(input())
    y = N*(1-X/100)
    dap = (N/y-1)*100
    print(f'{dap:.6f}')


if __name__ == '__main__':
    main()
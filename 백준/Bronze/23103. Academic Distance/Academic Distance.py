import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = 0
    x, y = map(int, input().split())
    for _ in range(N-1):
        a, b = map(int, input().split())
        dap += abs(x-a)+abs(y-b)
        x, y = a, b
    print(dap)


if __name__ == '__main__':
    main()
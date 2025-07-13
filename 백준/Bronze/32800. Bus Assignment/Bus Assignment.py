import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap, bus = 0, 0
    for _ in range(N):
        a, b = map(int, input().split())
        bus -= a
        bus += b
        dap = max(dap, bus)
    print(dap)


if __name__ == '__main__':
    main()
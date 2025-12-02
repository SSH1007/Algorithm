import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dap = 0
    N = int(input())
    for _ in range(N):
        h, w =map(int, input().split())
        dap = max(dap, h*w)
    print(dap)


if __name__ == '__main__':
    main()
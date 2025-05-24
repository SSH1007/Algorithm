import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, H = map(int, input().split())
    lst = list(map(int, input().split()))
    dap = 0
    for n in range(N):
        dap += lst[n]
        if dap >= H:
            print(n+1)
            exit(0)
    if dap < H:
        print(-1)


if __name__ == '__main__':
    main()
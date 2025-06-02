import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    lst = [int(input()) for _ in range(n)]
    dap = 0
    for i in range(1, n):
        if lst[i-1] - lst[i] >= k:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()
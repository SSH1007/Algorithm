import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    H, W = map(int, input().split())
    lst = list(map(int, input().split()))

    dap = 0
    for i in range(1, W-1):
        left_top = max(lst[:i])
        right_top = max(lst[i+1:])

        std = min(left_top, right_top)
        if std-lst[i] > 0:
            dap += (std-lst[i])
    print(dap)


if __name__ == '__main__':
    main()
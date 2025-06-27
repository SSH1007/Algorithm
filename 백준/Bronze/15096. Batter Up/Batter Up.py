import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    _ = int(input())
    ns = list(map(int, input().split()))
    dap, cnt = 0, 0
    for n in ns:
        if n != -1:
            dap += n
            cnt += 1
    print(dap/cnt)


if __name__ == '__main__':
    main()
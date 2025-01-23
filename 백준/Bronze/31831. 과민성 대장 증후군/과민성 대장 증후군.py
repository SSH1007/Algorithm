import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    s, dap = 0, 0
    for a in As:
        s = max(0, s+a)
        if s >= M:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()
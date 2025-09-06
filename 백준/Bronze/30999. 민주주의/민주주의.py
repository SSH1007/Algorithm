import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    dap = 0
    for _ in range(N):
        M = input()
        a, d = 0, 0
        for m in M:
            if m == 'O':
                a += 1
            else:
                d += 1
        if a > d:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()
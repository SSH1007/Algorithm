import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    a, b, n, k = map(int, input().split())
    dap = 0
    for x in range(1, a+1):
        for y in range(1, b+1):
            for _ in range(n):
                dap += 1
                if dap == k:
                    print(x, y)
                    return


if __name__ == '__main__':
    main()
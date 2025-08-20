import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    mx = float('inf')
    dap = 0
    for _ in range(n):
        c = int(input())
        if c <= mx:
            mx = c
        else:
            dap += (c-mx)
    print(dap)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    dap = 0
    while n > 1:
        if n%2 == 0:
            n //= 2
        else:
            n += 1
        dap += 1
    print(dap)


if __name__ == '__main__':
    main()
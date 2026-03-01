import sys
input = lambda: sys.stdin.readline().rstrip()


def F(n):
    i = 0
    for s in str(n):
        if i == 0 and s == '2':
            i = 1
        elif i == 1 and s == '0':
            i = 2
        elif i == 2 and s == '2':
            i = 3
        elif i == 3 and s == '3':
            return True
    return False


def main():
    N = int(input())
    if N < 2023:
        print(0)
    else:
        dap = 0
        for n in range(2023, N+1):
            if F(n):
                dap += 1
        print(dap)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    t1 = int(input())
    t2 = int(input())
    t3 = t1-t2
    dap = 2
    while t3 >= 0:
        t1 = t2
        t2 = t3
        t3 = t1-t2
        dap += 1
    print(dap)


if __name__ == '__main__':
    main()
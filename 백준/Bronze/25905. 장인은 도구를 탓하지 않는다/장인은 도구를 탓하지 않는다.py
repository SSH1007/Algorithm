import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    lst = []
    for _ in range(10):
        lst.append(float(input()))
    lst.sort()
    dap = 1
    for i in range(1, 10):
        dap *= lst[i]/i*10
    print(dap)


if __name__ == '__main__':
    main()
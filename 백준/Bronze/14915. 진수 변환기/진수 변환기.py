import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    m, n = map(int, input().split())
    if m == 0:
        print(0)
        return 0
    lst = []
    while m > 1:
        lst.append(m % n)
        m //= n
    if m:
        lst.append(m)
    dap = ''
    for i in range(len(lst)-1, -1, -1):
        if lst[i] > 9:
            dap += chr(lst[i]+55)
        else:
            dap += str(lst[i])
    print(dap)


if __name__ == '__main__':
    main()
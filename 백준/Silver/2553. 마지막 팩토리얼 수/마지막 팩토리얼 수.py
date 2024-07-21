import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = 1
    for n in range(1, N+1):
        dap *= n
    dap = str(dap)[::-1]
    for d in dap:
        if d != '0':
            print(d)
            break


if __name__ == '__main__':
    main()
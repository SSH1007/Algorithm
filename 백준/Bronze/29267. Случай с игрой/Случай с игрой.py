import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, k = map(int, input().split())
    save = 0
    dap, tmp = 0, 0
    for _ in range(n):
        m = input()
        if m == 'save':
            save = 1
            tmp = dap
        elif m == 'load':
            if save == 0:
                dap = 0
            else:
                dap = tmp
        elif m == 'shoot':
            dap -= 1
        else:
            dap += k
        print(dap)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    w = [2, 7, 6, 5, 4, 3, 2]
    c = 'JABCDEFGHIZ'
    N = input()
    dap = 0
    for n in range(7):
        dap += int(N[n])*w[n]
    print(c[dap%11])


if __name__ == '__main__':
    main()
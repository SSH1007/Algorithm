import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    a = '0123456789'
    b = 'abcdefghijklmnopqrstuvwxyz'
    c = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    d = '!@#$%^&*()-+'
    dap = 0
    for P in [a, b, c, d]:
        for n in P:
            if n in S:
                break
        else:
            dap += 1
    while N+dap < 6:
        dap += 1
    print(dap)


if __name__ == '__main__':
    main()
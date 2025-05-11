import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    dap = ''
    for _ in range(2*N-1):
        dap += input()
    dap = dap.replace('/', '//')
    print(eval(dap))


if __name__ == '__main__':
    main()
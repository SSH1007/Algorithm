import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = ['.'] + list(input())
    dap = 0
    for i in range(1, len(N)):
        if N[i] == 'Y':
            for j in range(i, len(N), i):
                if N[j] == 'Y':
                    N[j] = 'N'
                else:
                    N[j] = 'Y'
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()
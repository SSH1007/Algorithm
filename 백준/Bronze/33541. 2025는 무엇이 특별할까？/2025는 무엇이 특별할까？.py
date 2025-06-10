import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    X = int(input())+1
    dap = -1
    while X < 10000:
        if (X//100 + X%100)**2 == X:
            dap = X
            break
        X += 1
    print(dap)


if __name__ == '__main__':
    main()
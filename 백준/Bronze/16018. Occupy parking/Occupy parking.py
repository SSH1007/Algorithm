import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    T = input()
    Y = input()
    dap = 0
    for n in range(N):
        if T[n] == Y[n] and T[n] == 'C':
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()
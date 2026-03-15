import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    dap = ''
    for n in range(N):
        if n >= 2 and dap[-2] == 'P' and dap[-1] == 'S' and S[n] in '45':
            continue
        dap += S[n]
    print(dap)


if __name__ == '__main__':
    main()
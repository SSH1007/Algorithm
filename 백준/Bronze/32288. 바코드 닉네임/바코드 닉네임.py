import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    dap = ''
    for n in range(N):
        if S[n] == 'l':
            dap += 'L'
        else:
            dap += 'i'
    print(dap)


if __name__ == '__main__':
    main()
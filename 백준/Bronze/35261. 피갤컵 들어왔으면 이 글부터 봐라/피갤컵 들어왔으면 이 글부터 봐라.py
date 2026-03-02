import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dap = 5
    N = int(input())
    S = input()
    for n in range(N-4):
        tmp = 0
        if S[n] != 'e':
            tmp += 1
        if S[n+1] != 'a':
            tmp += 1
        if S[n+2] != 'g':
            tmp += 1
        if S[n+3] != 'l':
            tmp += 1
        if S[n+4] != 'e':
            tmp += 1
        dap = min(dap, tmp)
    print(dap)


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    S = input()
    i = 0
    dap = ''
    while 1:
        if S[i:i+3] == 'PS4' or S[i:i+3] == 'PS5':
            S = S[:i+2] + S[i+3:]
        else:
            dap += S[i]
            i += 1
        if i >= len(S):
            break
    print(dap)


if __name__ == '__main__':
    main()
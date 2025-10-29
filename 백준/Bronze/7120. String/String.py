import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    S = input()
    dap = S[0]
    for i in range(1, len(S)):
        if S[i-1] != S[i]:
            dap += S[i]
    print(dap)


if __name__ == '__main__':
    main()
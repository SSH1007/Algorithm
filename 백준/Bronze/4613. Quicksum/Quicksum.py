import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        S = input()
        if S == '#':
            break
        dap = 0
        for i in range(len(S)):
            if S[i] == ' ':
                continue
            dap += (ord(S[i])-64)*(i+1)
        print(dap)


if __name__ == '__main__':
    main()
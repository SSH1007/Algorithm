import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    p, w = map(int, input().split())
    S = input()
    lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
    dap = 0
    for i in range(len(S)):
        if S[i] == ' ':
            dap += p
        else:
            if i != 0:
                for l in lst:
                    if S[i] in l and S[i-1] in l:
                        dap += w
            for l in lst:
                if S[i] in l:
                    dap += p*(l.index(S[i])+1)
    print(dap)


if __name__ == '__main__':
    main()
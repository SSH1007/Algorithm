import sys
input = lambda: sys.stdin.readline().rstrip()


def CtoJ(S):
    dap = ''
    flag = 0
    if S[-1] == '_':
        return 'Error!'
    for s in S:
        if s == '_':
            if flag > 0:
                return 'Error!'
            flag += 1
        else:
            if s.isupper():
                return 'Error!'
            else:
                if flag:
                    dap += s.upper()
                    flag = 0
                else:
                    dap += s
    return dap


def JtoC(S):
    dap = ''
    for s in S:
        if s == '_':
            return 'Error!'
        if s.isupper():
            dap += '_'
        dap += s.lower()
    return dap


def main():
    S = input()
    if S[0] == '_' or S[0].isupper():
        print('Error!')
        exit(0)
    if len(S) == 1:
        if S.isupper():
            print('Error!')
        else:
            print(S)
    else:
        for s in S:
            if s == '_':
                print(CtoJ(S))
                break
        else:
            print(JtoC(S))


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        S = input()
        if S == '#':
            break
        c = 26-(ord(S[-1])-65)
        S = S[:-1]
        dap = ''
        for s in S:
            if 65 <= ord(s) <= 90:
                dap += chr((ord(s)-65+c)%26+65)
            elif 97 <= ord(s) <= 122:
                dap += chr((ord(s)-97+c)%26+97)
            else:
                dap += s
        print(dap)


if __name__ == '__main__':
    main()
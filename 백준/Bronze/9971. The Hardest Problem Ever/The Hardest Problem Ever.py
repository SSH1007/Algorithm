import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        S = input()
        if S == 'ENDOFINPUT':
            break
        elif S == 'END' or S == 'START':
            continue
        dap = ''
        for s in S:
            if s.isalpha():
                s = chr((ord(s)-65-5)%26+65)
            dap += s
        print(dap)


if __name__ == '__main__':
    main()
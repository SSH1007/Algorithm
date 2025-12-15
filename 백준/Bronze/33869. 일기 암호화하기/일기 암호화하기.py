import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    W = input()
    S = input()
    C = ''
    for w in W:
        if w not in C:
            C = C+w
    for i in range(26):
        tmp = chr(65+i)
        if tmp not in C:
            C = C + tmp
    dap = ''
    for s in S:
        dap = dap + C[ord(s)-65]
    print(dap)


if __name__ == '__main__':
    main()
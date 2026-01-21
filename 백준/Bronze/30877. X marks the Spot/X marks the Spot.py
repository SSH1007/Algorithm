import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dap = ''
    for _ in range(int(input())):
        S, T = input().split()
        j = 0
        for i in range(len(S)):
            if S[i] == 'x' or S[i] == 'X':
                j = i
                break
        tmp = T[j]
        if tmp.islower():
            tmp = chr(ord(tmp)-32)
        dap += tmp
    print(dap)


if __name__ == '__main__':
    main()
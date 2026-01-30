import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        lst = input().split()
        if lst[0] == '#':
            break
        num = []
        L = len(lst[0])
        for i in range(L):
            a = (ord(lst[1][i])-ord(lst[0][i]))%26
            num.append(a)
        dap = ''
        for i in range(L):
            dap += chr((ord(lst[2][i])+num[i]-97)%26+97)
        print(*lst, dap)


if __name__ == '__main__':
    main()
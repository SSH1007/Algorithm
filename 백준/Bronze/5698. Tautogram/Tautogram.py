import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        S = input()
        if S == '*':
            break
        lst = list(S.split())
        a = ''
        flag = True
        for l in lst:
            if a == '' and a != l[0].upper():
                a = l[0].upper()
            elif a != l[0].upper():
                flag = False
                break
        if flag:
            print('Y')
        else:
            print('N')


if __name__ == '__main__':
    main()
import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    dic = {' ':'%20', '!':'%21', '$':'%24', '%':'%25', '(':'%28', ')':'%29', '*':'%2a'}
    while 1:
        N = input()
        if N == '#':
            break
        tmp = ''
        for n in N:
            if n in dic:
                tmp += dic[n]
            else:
                tmp += n
        print(tmp)


if __name__ == '__main__':
    main()
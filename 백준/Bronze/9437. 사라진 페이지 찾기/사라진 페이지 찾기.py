import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        C = input()
        if C == '0':
            break
        else:
            N, P = map(int, C.split())
            lst = []
            for i in range(0, N//2, 2):
                tmp = []
                tmp.append(i+1)
                tmp.append(i+2)
                tmp.append(N-i-1)
                tmp.append(N-i)
                lst.append(tmp)
            for l in lst:
                if P in l:
                    for p in l:
                        if p != P:
                            print(p, end=' ')
            print()


if __name__ == '__main__':
    main()
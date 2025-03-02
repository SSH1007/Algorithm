import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    while 1:
        C = input()
        if C == '0':
            break
        else:
            N, P = map(int, C.split())
            n, p = N//2, (P+1)//2
            print(*sorted({2*p-1, 2*p, 2*(n-p+1), 2*(n-p+1)-1}-{P}))


if __name__ == '__main__':
    main()
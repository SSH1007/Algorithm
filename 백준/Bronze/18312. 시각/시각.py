import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, K = map(int, input().split())
    dap = 0
    a, b, c = 0, 0, 0
    while 1:
        if c > 59:
            c = 0
            b += 1
        if b > 59:
            b = 0
            a += 1
        tmp = str(a*10000+b*100+c)
        for i in range(6-len(tmp)):
            tmp = '0' + tmp
        if str(K) in tmp:
            dap += 1
        if a == N and b == 59 and c == 59:
            print(dap)
            break
        c += 1


if __name__ == '__main__':
    main()
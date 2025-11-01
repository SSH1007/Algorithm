import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    T = int(input())
    L = 'abcdefghijklmnopqrstuvwxyz '
    for _ in range(T):
        S = list(input().split())
        dap = ''
        for s in S:
            tmp = 0
            for _s in s:
                tmp += ord(_s)-97
            dap += L[tmp%27]
        print(dap)


if __name__ == '__main__':
    main()
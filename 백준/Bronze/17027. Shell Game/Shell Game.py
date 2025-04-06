import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    dap = 0
    for i in range(1, 4):
        tmp = 0
        for n in range(N):
            a, b, g = lst[n]
            if i == a:
                i = b
            elif i == b:
                i = a
            if i == g:
                tmp += 1
        if dap < tmp:
            dap = tmp
    print(dap)


if __name__ == '__main__':
    main()
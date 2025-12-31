import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    for _ in range(N):
        lst = list(input().split())
        tmp, dap = True, 0
        if len(lst) > 1:
            tmp = False
        try:
            if int(lst[0]) < 0:
                tmp = False
            else:
                dap = int(lst[0])
        except:
            tmp = False
        if tmp:
            print(dap)
        else:
            print('invalid input')


if __name__ == '__main__':
    main()
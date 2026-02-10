import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    lst = []
    for _ in range(N):
        lst.append(input())
    o, t = 0, 0
    dap = ''
    for i in range(N):
        if lst[i] == 'KBS1':
            o = i
            dap = '1'*o+'4'*o
            break
    for i in range(N):
        if lst[i] == 'KBS2':
            t = i+1 if o > i else i
            dap = dap + '1'*t+'4'*(t-1)
            break
    print(dap)


if __name__ == '__main__':
    main()
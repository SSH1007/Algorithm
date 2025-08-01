import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n = int(input())
    dap = 0
    lst = []
    for i in range(1, n+1):
        t, s = map(int, input().split())
        lst.append((i, t, s))
    lst.sort(key=lambda x: (-x[2], x[1]))
    if lst[0][2] == 1 or lst[0][2] == 4:
        dap = lst[0][1] + (lst[0][0]-1)*20
    print(dap)


if __name__ == '__main__':
    main()
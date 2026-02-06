import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    cnt = 1
    while 1:
        n = int(input())
        if n == 0:
            break
        dap = 0
        for i in range(n):
            lst = list(map(int, input().split()))
            if i == 0 or i == n-1:
                dap += sum(lst)
            else:
                dap += (lst[0]+lst[-1])
        print(f'Case #{cnt}:{dap}')
        cnt += 1


if __name__ == '__main__':
    main()
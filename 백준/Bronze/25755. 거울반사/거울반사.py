import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    W, N = input().split()
    N = int(N)
    lst = [list(map(int, input().split())) for _ in range(N)]
    dic = {1:1, 2:5, 5:2, 8:8}
    dap = [[0]*N for _ in range(N)]
    for n in range(N):
        for m in range(N):
            tmp = lst[n][m]
            if W == 'U' or W == 'D':
                if dic.get(tmp):
                    dap[N-n-1][m] = dic[tmp]
                else:
                    dap[N-n-1][m] = '?'
            else:
                if dic.get(tmp):
                    dap[n][N-m-1] = dic[tmp]
                else:
                    dap[n][N-m-1] = '?'
    for d in dap:
        print(*d)


if __name__ == '__main__':
    main()
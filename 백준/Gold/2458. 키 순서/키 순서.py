import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    lst = [[0]*(N+1) for _ in range(N+1)]
    for i in range(1, N+1):
        for j in range(1, N+1):
            if i == j:
                lst[i][j] = 2
    for _ in range(M):
        a, b = map(int, input().split())
        lst[a][b] = 1
        lst[b][a] = 3
    for k in range(1, N+1):  # 경유
        for i in range(1, N+1):  # 출발
            for j in range(1, N+1):  # 도착
                if i == j:
                    continue
                if lst[i][k] == lst[k][j] and lst[i][k] != 0:
                    lst[i][j] = lst[i][k]
    dap = 0
    for l in lst:
        if l[1:].count(0) == 0:
            dap += 1
    print(dap)


if __name__ == '__main__':
    main()
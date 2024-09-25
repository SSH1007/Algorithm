import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    n, m, r = map(int, input().split())
    items = list(map(int, input().split()))
    inf = int(1e9)
    maps = [[inf]*(n+1) for _ in range(n+1)]
    # 초기화(i에서 i로 가는 길이는 0)
    for i in range(1, n+1):
        maps[i][i] = 0

    for _ in range(r):
        a, b, l = map(int, input().split())
        maps[a][b] = l
        maps[b][a] = l

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if maps[i][j] > maps[i][k] + maps[k][j]:
                    maps[i][j] = maps[i][k] + maps[k][j]

    dap = 0
    for i in range(1, n+1):
        tmp = 0
        for j in range(1, n+1):
            # 수색범위 이내라면
            if maps[i][j] <= m:
                tmp += items[j-1]
        dap = max(dap, tmp)
    print(dap)


if __name__ == '__main__':
    main()
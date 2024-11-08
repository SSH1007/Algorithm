import sys
input = lambda: sys.stdin.readline().rstrip()


inf = float('inf')


def F(V, maps):
    for k in range(1, V+1):
        for i in range(1, V+1):
            for j in range(1, V+1):
                if maps[i][j] > maps[i][k]+maps[k][j]:
                    maps[i][j] = maps[i][k]+maps[k][j]

    dap = inf
    for i in range(1, V+1):
        dap = min(dap, maps[i][i])
    return -1 if dap == inf else dap


def main():
    V, E = map(int, input().split())
    maps = [[inf]*(V+1) for _ in range(V+1)]
    for _ in range(E):
        a, b, c = map(int, input().split())
        maps[a][b] = c
    print(F(V, maps))


if __name__ == '__main__':
    main()
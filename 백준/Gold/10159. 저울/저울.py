import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N = int(input())
    M = int(input())
    maps = [[0]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b = map(int, input().split())
        maps[a][b] = 1    # a > b
        maps[b][a] = -1   # b < a

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                # ex) 1 > 2 and 2 > 3 => 1 > 3
                if maps[i][k] == 1 and maps[k][j] == 1:
                    maps[i][j] = 1
                if maps[i][k] == -1 and maps[k][j] == -1:
                    maps[i][j] = -1

    for n in range(1, N+1):
        print(maps[n][1:].count(0)-1)


if __name__ == '__main__':
    main()
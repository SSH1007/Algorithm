import sys
input = lambda: sys.stdin.readline().rstrip()


def fw():
    for k in range(1, N+1):
        maps[k][k] = 0
        for i in range(1, N+1):
            for j in range(1, N+1):
                if maps[i][j] > maps[i][k] + maps[k][j]:
                    maps[i][j] = maps[i][k] + maps[k][j]


T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    inf = float('inf')
    maps = [[inf]*(N+1) for _ in range(N+1)]
    for _ in range(M):
        a, b, c = map(int, input().split())
        maps[a][b] = c
        maps[b][a] = c
    As = [0]*(N+1)
    K = int(input())
    friends = list(map(int, input().split()))
    fw()
    for f in friends:
        for n in range(N+1):
            As[n] += maps[f][n]
    maxIdx, minVal = 0, inf
    for n in range(1, N+1):
        if minVal > As[n]:
            minVal = As[n]
            maxIdx = n
    print(maxIdx)
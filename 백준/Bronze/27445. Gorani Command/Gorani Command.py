import sys
input = lambda: sys.stdin.readline().rstrip()


def main():
    N, M = map(int, input().split())
    lst = [[0]*M for _ in range(N)]
    for n in range(N-1):
        lst[n][0] = int(input())
    Ms = list(map(int, input().split()))
    for m in range(M):
        lst[N-1][m] = Ms[m]
    inf = float('inf')
    minN, minM = inf, inf
    x, y = 0, 0
    for n in range(N):
        if minN > lst[n][0]:
            minN = lst[n][0]
            y = n
    for m in range(M):
        if minM > lst[N-1][m]:
            minM = lst[N-1][m]
            x = m
    print(y+1, x+1)


if __name__ == '__main__':
    main()
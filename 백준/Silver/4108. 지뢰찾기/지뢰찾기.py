import sys
input = sys.stdin.readline
dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]
while 1:
    N, M = map(int, input().rstrip().split())
    if N == 0 and M == 0:
        break
    mine = [list(input()) for _ in range(N)]
    dap = [['']*M for _ in range(N)]
    for n in range(N):
        for m in range(M):
            if mine[n][m] == '*':
                dap[n][m] = '*'
            else:
                tmp = 0
                for i in range(8):
                    nm = m+dx[i]
                    nn = n+dy[i]
                    if 0<=nm<M and 0<=nn<N:
                        if mine[nn][nm] == '*':
                            tmp += 1
                dap[n][m] = str(tmp)
    for d in dap:
        print(*d, sep='')
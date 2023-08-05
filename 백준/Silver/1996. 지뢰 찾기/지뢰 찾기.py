import sys
input = sys.stdin.readline
N = int(input().rstrip())
mine = [list(input().rstrip()) for _ in range(N)]
dap = [['']*N for _ in range(N)]
dx = [0,1,1,1,0,-1,-1,-1]
dy = [-1,-1,0,1,1,1,0,-1]

for i in range(N):
    for j in range(N):
        if mine[i][j] != '.':
            dap[i][j] = '*'
        else:
            tmp = 0
            for k in range(8):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0<=ni<N and 0<=nj<N:
                    if mine[ni][nj] != '.':
                        tmp += int(mine[ni][nj])
            if tmp > 9:
                dap[i][j] = 'M'
            else:
                dap[i][j] = str(tmp)
for d in dap:
    print(*d, sep='')
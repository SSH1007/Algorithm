H, W = map(int, input().split())
info = [input() for _ in range(H)]
dap = [[0]*W for _ in range(H)]

for i in range(H):
    cloud = False
    for j in range(W):
        if cloud and info[i][j] != 'c':
            dap[i][j] = dap[i][j-1]+1
        elif info[i][j] != 'c':
            dap[i][j] = -1
        if info[i][j] == 'c':
            cloud = True


for d in dap:
    print(*d)
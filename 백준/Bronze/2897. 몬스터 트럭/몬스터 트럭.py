R, C = map(int, input().split())
park = [list(input()) for _ in range(R)]
dap = [0, 0, 0, 0, 0, 0]
dr = [0, 1, 0, 1]
dc = [0, 0, 1, 1]
for i in range(R-1):
    for j in range(C-1):
        tmp = 0
        for k in range(4):
            ni = i + dr[k]
            nj = j + dc[k]
            if park[ni][nj] == '#':
                tmp = -1
                break
            elif park[ni][nj] == 'X':
                tmp += 1
        dap[tmp] += 1
for d in dap[:-1]:
    print(d)
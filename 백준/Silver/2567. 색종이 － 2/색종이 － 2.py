N = int(input())
paper = [[0]*101 for _ in range(101)]
for _ in range(N):
    x, y = map(int, input().split())
    for i in range(x,x+10):
        for j in range(y,y+10):
            paper[i][j] = 1

dr = [-1,1,0,0]
dc = [0,0,-1,1]
dap = 0
for i in range(101):
    for j in range(101):
        if paper[i][j]:
            for k in range(4):
                if not paper[i+dr[k]][j+dc[k]]:
                    dap += 1

print(dap)
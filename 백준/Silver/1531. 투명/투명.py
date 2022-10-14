canvas = [[0]*100 for _ in range(100)]
N, M = map(int, input().split())
for _ in range(N):
    x1,y1, x2,y2 = map(int, input().split())
    for x in range(x1-1, x2):
        for y in range(y1-1,y2):
            canvas[x][y]+=1
dap = 0
for cvs in canvas:
    for c in cvs:
        if c>M:
            dap+=1
print(dap)
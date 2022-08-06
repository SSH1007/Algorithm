import sys
input = sys.stdin.readline
matrix = [[0]*101 for _ in range(101)]
for _ in range(4):
    a,b,c,d = map(int,input().split())
    for i in range(a,c):
        for j in range(b,d):
            matrix[i][j]=1
dap = 0
for m in matrix:
    dap+=sum(m)
print(dap)
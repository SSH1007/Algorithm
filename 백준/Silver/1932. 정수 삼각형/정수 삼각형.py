import sys
input = sys.stdin.readline
N = int(input().rstrip())
tri = []
for _ in range(N):
    tri.append(list(map(int ,input().rstrip().split())))
dap = [[0 for _ in range(N)] for _ in range(N)]
dap[0][0] = tri[0][0]
for i in range(N-1):
    for j in range(len(tri[i+1])):
        if dap[i+1][j] < dap[i][j]+tri[i+1][j]:
            dap[i+1][j] = dap[i][j]+tri[i+1][j]
        if dap[i+1][j] < dap[i][j-1]+tri[i+1][j]:
            dap[i+1][j] = dap[i][j-1]+tri[i+1][j]
print(max(dap[-1]))
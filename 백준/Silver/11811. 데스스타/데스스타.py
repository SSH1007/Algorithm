import sys
input = sys.stdin.readline
N = int(input().rstrip())
matrix = [list(map(int, input().rstrip().split())) for _ in range(N)]
dap = [0]*N
for i in range(N):
    for j in range(N):
        dap[i] = dap[i] | matrix[i][j]
print(*dap)
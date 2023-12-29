R, C, W = map(int, input().split())
mat = [[0]*(R+W) for _ in range(R+W)]
mat[0][0] = 1
mat[1][0], mat[1][1] = 1, 1

for i in range(2, R+W):
    for j in range(R+W):
        mat[i][j] = mat[i-1][j] + mat[i-1][j-1]
dap = 0
tri = 1
for i in range(R-1, R-1+W):
    for j in range(C-1, C-1+tri):
        dap += mat[i][j]
    tri += 1
print(dap)
N = int(input())
where = int(input())
mat = [[0]*N for _ in range(N)]

width = N
news = 1
r, c = -1, 0
num = N**2

while width > 0:
    for _ in range(width):
        r += news
        mat[r][c] = num
        num -= 1
    width -= 1
    for _ in range(width):
        c += news
        mat[r][c] = num
        num -= 1
    news *= -1

dap = []
for i in range(N):
    for j in range(N):
        if mat[i][j] == where:
            dap.extend((i+1, j+1))
        print(mat[i][j], end=' ')
    print()
print(*dap)
N = int(input())
l = N*4-3
mat = [[' ']*l for _ in range(l)]


def f(n, r, c):
    if n == 1:
        mat[r][c] = '*'
        return
    l = n*4-3
    for i in range(l):
        mat[r][c+i] = '*'  #상
        mat[r+i][c] = '*'  #좌
        mat[l+r-1][c+i] = '*'  #하
        mat[r+i][l+c-1] = '*'  #우

    f(n-1, r+2, c+2)


f(N, 0, 0)

for m in mat:
    print(''.join(m))
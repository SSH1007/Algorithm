n, k = map(int, input().split())
tri = [[1]*(n+1) for _ in range(n)]

for i in range(2, n):
    for j in range(1, i):
        tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

print(tri[n-1][k-1])
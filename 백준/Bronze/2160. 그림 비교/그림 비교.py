import sys
input = sys.stdin.readline
N = int(input().rstrip())
pic = []
for _ in range(N):
    lst = [list(input().rstrip()) for _ in range(5)]
    pic.append(lst)


def F(i, j):
    d = 0
    for r in range(5):
        for c in range(7):
            if pic[i][r][c] != pic[j][r][c]:
                d += 1
    return d


dap = 100
a, b = 0, 0
for i in range(N):
    for j in range(i+1, N):
        nDap = F(i, j)
        if dap > F(i, j):
            a, b = i+1, j+1
            dap = nDap

print(a, b)
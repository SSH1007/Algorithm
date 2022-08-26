import sys

matrix = [[0]*1001 for _ in range(1001)]

N = int(input())
for n in range(1, N+1):
    x, y, w, h = map(int,sys.stdin.readline().split())
    for i in range(x, x+w):
        matrix[i][y: y+h] = [n]*h

for n in range(1, N+1):
    hap = 0
    for r in matrix:
        hap += r.count(n)
    print(hap)
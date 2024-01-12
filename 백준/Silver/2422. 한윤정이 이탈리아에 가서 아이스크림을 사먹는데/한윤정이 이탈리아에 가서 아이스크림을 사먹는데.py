import sys
input = sys.stdin.readline
from itertools import combinations
N, M = map(int, input().rstrip().split())
lst = [[1]*N for _ in range(N)]
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    lst[a-1][b-1] = 0
    lst[b-1][a-1] = 0

dap = 0
for i in combinations(range(N), 3):
    if lst[i[0]][i[1]] and lst[i[1]][i[2]] and lst[i[2]][i[0]]:
       dap += 1
print(dap)
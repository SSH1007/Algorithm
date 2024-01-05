import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
for _ in range(N):
    x, y = map(int, input().rstrip().split())
    lst.append((x, y))

lst.sort(key=lambda x: (x[1], x[0]))
lst = [(0, -1)]+lst+[(0, -1)]

dap = 0
for i in range(1, N+1):
    if lst[i][1] == lst[i+1][1] and lst[i][1] != lst[i-1][1]:
        dap += (lst[i+1][0] - lst[i][0])
    elif lst[i-1][1] == lst[i][1] and lst[i][1] != lst[i+1][1]:
        dap += (lst[i][0] - lst[i-1][0])
    elif lst[i-1][1] == lst[i][1] and lst[i+1][1] == lst[i][1]:
        dap += min(lst[i][0]-lst[i-1][0], lst[i+1][0]-lst[i][0])

print(dap)
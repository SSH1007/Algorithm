import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
x, y = map(int, input().rstrip().split())
lst = [(x, y)]
for n in range(1, N):
    x, y = map(int, input().rstrip().split())
    lst.append((x, y))
    a = abs(x-lst[n-1][0])
    b = abs(y-lst[n-1][1])
    dap += (a+b)
a = abs(lst[N-1][0] - lst[0][0])
b = abs(lst[N-1][1] - lst[0][1])
dap += (a+b)
print(dap)
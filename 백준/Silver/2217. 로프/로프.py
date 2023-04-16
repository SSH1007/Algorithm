import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
lst = []
for _ in range(N):
    lst.append(int(input().rstrip()))
lst.sort()
for i in range(N):
    if dap < lst[i]*(N-i):
        dap = lst[i]*(N-i)
print(dap)
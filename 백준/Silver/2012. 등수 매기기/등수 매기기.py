import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
for _ in range(N):
    lst.append(int(input().rstrip()))
lst.sort()
dap = 0
for i in range(N):
    dap += abs((i+1)-lst[i])
print(dap)
import sys
input = lambda: sys.stdin.readline().rstrip()


N = int(input())
lst = list(map(int, input().split()))
k = int(input())

i = N//k
dap = []
for j in range(0, N, i):
    dap.extend(sorted(lst[j:j+i]))
print(*dap)
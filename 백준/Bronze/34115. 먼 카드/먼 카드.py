N = int(input())
X = list(map(int, input().split()))
lst = [[] for _ in range(N)]
for n in range(2*N):
    lst[X[n]-1].append(n)
dap = 0
for l in lst:
    dap = max(dap, l[1]-l[0]-1)
print(dap)
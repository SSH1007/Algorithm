import sys
input = sys.stdin.readline
N, K = map(int, input().rstrip().split())
lst = list(map(int, input().rstrip().split()))
dap = []
A = sum(lst[:K])
dap.append(A)
for i in range(N-K):
    A -= lst[i]
    A += lst[i+K]
    dap.append(A)
print(max(dap))
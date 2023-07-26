N, M = map(int, input().split())
ks = list(map(int, input().split()))
lst = [0 for _ in range(1001)]
dap = 0
for k in ks:
    for i in range(k, N+1, k):
        lst[i] = 1

for n in range(1001):
    if lst[n] == 1:
        dap += n
print(dap)
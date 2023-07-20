N = int(input())
K = int(input())
lst = [0 for _ in range(N+1)]
for i in range(2, N+1):
    if not lst[i]:
        for j in range(i, N+1, i):
            lst[j] = max(lst[j], i)

dap = 0
for n in range(1, N+1):
    if lst[n] <= K:
        dap += 1
print(dap)
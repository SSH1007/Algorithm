N = int(input())
lst = list(map(int, input().split()))
lst.sort(reverse=True)
dap = []
for n in range(N):
    dap.append(lst[n]+1+n)
print(max(dap)+1)
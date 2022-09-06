N = int(input())
lst = list(map(int, input().split()))
lst.sort()
dap = 0
for n in range(1,N+1):
    dap+=sum(lst[:n])
print(dap)
dap = 0
N = int(input())
lst = list(map(int, input().split()))
for i in range(1, N):
    if lst[i]>lst[i-1]:
        dap+=1
print(dap)
N = int(input())
dap=0
for _ in range(N):
    x = input().split('-')
    if int(x[1])<=90:
        dap+=1
print(dap)
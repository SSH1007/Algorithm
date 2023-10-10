N = int(input())
c = 1
for n in range(1, N+1):
    c *= n
dap = c//(7*24*60*60)
print(dap)
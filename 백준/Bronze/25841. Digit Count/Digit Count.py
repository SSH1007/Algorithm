a, b, c = map(int, input().split())
dap = 0
for i in range(a, b+1):
    dap += str(i).count(str(c))
print(dap)
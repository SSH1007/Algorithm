A, B = map(int, input().split())
l = [0]
for i in range(1, 46):
    l.extend([i]*i)
dap = 0
for n in range(A, B+1):
    dap += l[n]
print(dap)
h = 0
dap = 0
for _ in range(10):
    a, b = map(int,input().split())
    h-=a
    h+=b
    if h>dap:
        dap=h
print(dap)
T = int(input())
dap = (T/2)**2
if dap%1 >= 0.5:
    print(int(dap)+1)
else:
    print(int(dap))
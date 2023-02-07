N = int(input())
dap = 3
for n in range(1,N):
    dap+=2**n
print(dap**2)
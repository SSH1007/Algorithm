N = input()
dap = ''
for n in range(len(N)):
    dap = N[len(N)-1-n] + dap
    if n % 3 == 2 and n != len(N)-1:
        dap = ',' + dap
print(dap)
dap = 0
N = int(input())
for n in range(N+1):
    if '3' or '6' or '9' in str(n):
        dap+=str(n).count('3')
        dap+=str(n).count('6')
        dap+=str(n).count('9')
print(dap)
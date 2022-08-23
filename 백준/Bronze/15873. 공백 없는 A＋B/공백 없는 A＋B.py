AB = input()
dap = 0
for i in range(len(AB)):
    if i<len(AB)-1 and AB[i+1] == '0':
        dap+=int(AB[i])*10
    else:
        dap+=int(AB[i])
print(dap)
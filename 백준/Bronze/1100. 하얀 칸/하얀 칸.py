dap = 0
chesspan = [list(input()) for _ in range(8)]
for line in range(len(chesspan)):
    if line%2:
        for p in range(8):
            if p%2!=0 and chesspan[line][p]=='F':
                dap+=1
    else:
        for p in range(8):
            if p%2==0 and chesspan[line][p]=='F':
                dap+=1
print(dap)
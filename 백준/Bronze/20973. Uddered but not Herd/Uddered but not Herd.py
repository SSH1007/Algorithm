S = input()
B = input()
dap = 1
i = 0
for b in B:
    while 1:
        if i > 25:
            i = 0
            dap += 1
        if S[i] == b:
            i += 1
            break
        i +=1 
print(dap)
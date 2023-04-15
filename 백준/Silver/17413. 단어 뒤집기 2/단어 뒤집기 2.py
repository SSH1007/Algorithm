S = input()
dap = []
tmp = []
for i in range(len(S)):
    if S[i]==' ' and  '<' not in tmp:
        dap.append(''.join(tmp[::-1])+' ')
        tmp = []
    elif S[i]=='<' and tmp:
        dap.append(''.join(tmp[::-1]))
        tmp = []
        tmp.append('<')
    elif S[i]=='>':
        dap.append(''.join(tmp)+'>')
        tmp = []
    else:
        tmp.append(S[i])
print(*dap, sep='', end='')
print(''.join(tmp[::-1]))
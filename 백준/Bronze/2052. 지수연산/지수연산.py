N = int(input())
dap = '%.250f'%(2**(-N))
end = 1e9
for i in range(len(dap)-1, 0, -1):
    if dap[i]!='0':
        end = i
        break
print(dap[:end+1])
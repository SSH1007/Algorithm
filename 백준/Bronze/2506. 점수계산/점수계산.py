_ = int(input())
dap = 0
N = ''.join(input().split()).split('0')
for nn in N:
    for n in range(1,len(nn)+1):
        dap+=n
print(dap)
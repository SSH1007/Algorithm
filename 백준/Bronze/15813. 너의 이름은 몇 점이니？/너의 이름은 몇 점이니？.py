N = int(input())
S = input()
alpha = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
dap = 0
for s in S:
    dap += (alpha.index(s)+1)
print(dap)
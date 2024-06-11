S = input()
aCnt = S.count('a')
S += S
dap = 1000
for i in range(len(S)//2):
    dap = min(dap, S[i:i+aCnt].count('b'))
print(dap)
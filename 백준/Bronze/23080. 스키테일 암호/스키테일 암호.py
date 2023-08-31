K = int(input())
S = input()
i = 0
dap = ''
while i < len(S):
    dap += S[i]
    i += K
print(dap)
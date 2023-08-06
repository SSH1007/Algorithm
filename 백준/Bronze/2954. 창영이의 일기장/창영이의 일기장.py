S = input()
dap = ''
idx = 0
while idx < len(S):
    if S[idx] in ['a', 'e', 'i', 'o', 'u']:
        dap += S[idx]
        idx += 3
    else:
        dap += S[idx]
        idx += 1
print(dap)
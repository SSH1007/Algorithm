S = input()
ls = len(S)
dap = 1
if S[0] == 'c':
    dap *= 26
else:
    dap *= 10
if ls > 1:
    for n in range(1, len(S)):
        if S[n] == S[n-1] and S[n] == 'c':
            dap *= 25
        elif S[n] != S[n-1] and S[n] == 'c':
            dap *= 26
        elif S[n] == S[n-1] and S[n] == 'd':
            dap *= 9
        else:
            dap *= 10
print(dap)
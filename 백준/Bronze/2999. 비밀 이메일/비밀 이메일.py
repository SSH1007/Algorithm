S = input()
std = int(len(S)**0.5)+1
R, C = 0, 0
for i in range(std, 0, -1):
    if len(S)%i == 0:
        R = i
        C = len(S)//i
        if R<=C:
            break

dap = ''
for r in range(R):
    for c in range(r, len(S), R):
        dap += S[c]
print(dap)
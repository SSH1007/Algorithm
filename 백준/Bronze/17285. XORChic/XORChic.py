S = input()
dap = ''
K = ord(S[0])^ord('C')
for s in S:
    dap += chr(ord(s)^K)
print(dap)
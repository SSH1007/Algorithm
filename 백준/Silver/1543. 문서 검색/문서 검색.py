S = input()
s = input()
Sl = len(S)
sl = len(s)
start, end = 0, sl
dap = 0
while start < Sl:
    if S[start:end] == s:
        dap += 1
        start += sl
        end += sl
    else:
        start += 1
        end += 1
print(dap)
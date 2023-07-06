str = input()
dap = ''
for s in str:
    if ord(s)>96:
        dap += chr(ord(s)-32)
    else:
        dap += chr(ord(s)+32)
print(dap)
        
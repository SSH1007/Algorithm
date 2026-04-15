str = input()
dap = ''
for s in str:
    if s.isupper():
        dap += s.lower()
    else:
        dap += s.upper()
print(dap)
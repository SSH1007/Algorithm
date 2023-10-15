T = int(input())
dap = 0
for _ in range(T):
    before = ''
    log = input()
    for l in log:
        if before == 'C' and l == 'D':
            break
        if l == 'C':
            before = 'C'
        else:
            before = ''
    else:
        dap += 1
print(dap)
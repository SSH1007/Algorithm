import sys
input = sys.stdin.readline
dap = 0
while 1:
    I = input().rstrip()
    if I == '':
        break
    s, e = I.split()
    if s == 'Es':
        dap += (21*int(e))
    else:
        dap += (17*int(e))
print(dap)
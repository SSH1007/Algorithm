dap = 0
def route(N):
    global dap
    dap = 0
    for n in N:
        dap+=int(n)
    if dap<10:
        return dap
    route(str(dap))
    

import sys
input = sys.stdin.readline
while 1:
    N = input().rstrip()
    if N == '0':
        break
    route(N)
    print(dap)
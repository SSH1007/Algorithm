import sys
input = sys.stdin.readline
fact = [0,1,2,6,24,120]
daps = []
while 1:
    N = int(input().rstrip())
    if N == 0:
        break
    dap = 0
    for i in range(len(str(N))):
        tmp = int(str(N)[i])*fact[len(str(N))-i]
        dap+=tmp
    daps.append(dap)
for d in daps:
    print(d)
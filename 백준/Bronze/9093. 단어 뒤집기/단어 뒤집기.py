import sys
input = sys.stdin.readline
T = int(input().rstrip())
daps = []
for _ in range(T):
    lst = list(input().rstrip().split())
    dap = ''
    for l in lst:
        dap += l[::-1]
        dap += ' '
    daps.append(dap[:-1])
for d in daps:
    print(d)
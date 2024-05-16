import sys
input = sys.stdin.readline
n = int(input().rstrip())
scroll = input().rstrip()
dap = 0
s, e = 0, 4
while e <= n:
    if scroll[s:e] == 'pPAp':
        dap += 1
        s += 4
        e += 4
    else:
        s += 1
        e += 1
print(dap)
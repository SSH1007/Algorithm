import sys
input = sys.stdin.readline
N = input().rstrip()
dap = ''
i = 0
while i < len(N):
    dap += N[i]
    i += (ord(N[i])-64)
print(dap)
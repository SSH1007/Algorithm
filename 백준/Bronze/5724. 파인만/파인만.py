import sys
input = sys.stdin.readline
while 1:
    N = int(input().rstrip())
    if N == 0:
        break
    dap = 0
    for n in range(N):
        dap += (n+1)**2
    print(dap)
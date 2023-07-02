import sys
input = sys.stdin.readline

A, K = map(int, input().rstrip().split())
dap = 0
while 1:
    if K==A:
        print(dap)
        break
    if K%2==0 and K>=A*2:
        K//=2
    else:
        K-=1
    dap+=1
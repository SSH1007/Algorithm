import sys
input = sys.stdin.readline
N = int(input())
dap = 0
for n in range(N):
    i = int(input())
    if n != N-1:
        dap+=(i-1)
    else:
        dap+=i 
print(dap) 
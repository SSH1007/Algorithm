import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
start, end = 1, 2
while start<500:
    if end**2 - start**2 == N:
        dap+=1
        start+=1
        end = start+1
    elif end>500:
        start+=1
        end = start+1
    else:
        end += 1
print(dap)
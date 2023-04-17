import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int,input().rstrip().split()))
dap = 0
for n in range(N):
    if n+1!=lst[n]:
        dap+=1
print(dap)
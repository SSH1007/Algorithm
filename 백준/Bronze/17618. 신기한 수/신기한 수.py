import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
for n in range(1, N+1):
    if n%sum(map(int, str(n)))==0:
        dap+=1
print(dap)
import sys
input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    dap = 0
    m = int(input().rstrip())
    for _ in range(m):
        lst = list(input().rstrip().split())
        dap+=(int(lst[1])*float(lst[2]))
    print(f'${dap:.2f}')
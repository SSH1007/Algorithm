import sys
input = sys.stdin.readline
K = int(input())
for i in range(1,K+1):
    n, s, d = map(int, input().split())
    dap = 0
    for _ in range(n):
        di, vi = map(int, input().split())
        if d*s >= di:
            dap+=vi
    if i != 1:
        print()
    print(f'Data Set {i}:')
    print(dap)
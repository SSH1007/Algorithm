import sys
input = sys.stdin.readline
Q = int(input().rstrip())
dap = []
for _ in range(Q):
    a = int(input().rstrip())
    aa = (a&(-a)==a)
    dap.append(aa)
for d in dap:
    print(1 if d else 0)
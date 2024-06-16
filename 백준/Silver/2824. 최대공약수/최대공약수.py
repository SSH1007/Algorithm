import sys
input = sys.stdin.readline
N = int(input().rstrip())
Ns = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
Ms = list(map(int, input().rstrip().split()))


def GCD(a, b):
    while a != 0:
        a, b = b%a, a
    return b


A, B = 1, 1
for n in Ns:
    A*=n
for m in Ms:
    B*=m

dap = str(GCD(A, B))
if len(dap) > 9:
    print(dap[len(dap)-9:])
else:
    print(dap)
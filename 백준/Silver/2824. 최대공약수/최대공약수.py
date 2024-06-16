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

print('%s'%(str(GCD(A, B))[-9:]))
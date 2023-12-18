import sys
input = sys.stdin.readline
N = int(input().rstrip())
tree = [int(input().rstrip()) for _ in range(N)]
lst = [tree[i+1]-tree[i] for i in range(N-1)]


def GCD(a, b):
    while b>0:
        a, b = b, a%b
    return a


gcd = lst[-1]
for i in range(len(lst)):
    gcd = GCD(gcd, lst[i])

dap = 0
for i in range(N-1):
    dap += ((tree[i+1]-tree[i])//gcd-1)
print(dap)
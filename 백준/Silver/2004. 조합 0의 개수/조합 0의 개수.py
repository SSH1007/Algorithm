import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
# 10의 개수 = 2와 5의 개수

def getCnt(N, n):
    dap = 0
    while N > 0:
        N //= n
        dap += N
    return dap

two = getCnt(n,2) - getCnt(n-m, 2) - getCnt(m,2)
five = getCnt(n,5) - getCnt(n-m, 5) - getCnt(m,5)
print(min(two, five))
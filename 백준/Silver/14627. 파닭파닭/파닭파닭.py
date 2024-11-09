import sys
input = lambda: sys.stdin.readline().rstrip()


S, C = map(int, input().split())
s, e = 1, 0
lst = []
for _ in range(S):
    L = int(input())
    lst.append(L)
    if e < L:
        e = L

dap = 0
while s <= e:
    mid = (s+e)//2
    tmp = 0
    for l in lst:
        tmp += l//mid
    if tmp < C:
        e = mid - 1
    else:
        s = mid + 1
        dap = mid
print(sum(lst) - dap*C)
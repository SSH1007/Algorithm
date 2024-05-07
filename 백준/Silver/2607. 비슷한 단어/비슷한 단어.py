import sys
input = sys.stdin.readline
from copy import deepcopy
N = int(input().rstrip())
first = list(input().rstrip())
L = len(first)
dap = 0
for _ in range(N-1):
    another = input().rstrip()
    compare = deepcopy(first)
    cnt = 0
    for a in another:
        if a in compare:
            compare.remove(a)
        else:
            cnt += 1
    if cnt < 2 and len(compare) < 2:
        dap += 1
print(dap)
# 투 포인터 + defaultdict
import sys
input = sys.stdin.readline
from collections import defaultdict
N, K = map(int, input().rstrip().split())
As = list(map(int, input().rstrip().split()))
dd = defaultdict(int)
s, e = 0, 0
dap = 0
while e < N:
    if dd[As[e]] < K:
        dd[As[e]] += 1
        e += 1
    else:
        dd[As[s]] -= 1
        s += 1
    dap = max(dap, e-s)
print(dap)
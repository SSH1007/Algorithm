import sys
input = sys.stdin.readline
K = int(input().rstrip())
for k in range(K):
    n, W, E = map(int, input().rstrip().split())
    dap = 0
    for _ in range(n):
        ww, we, ew, ee = map(int, input().rstrip().split())
        dap += max(ww*W+ew*E, we*W+ee*E)
    print(f'Data Set {k+1}:')
    print(dap)
    print()
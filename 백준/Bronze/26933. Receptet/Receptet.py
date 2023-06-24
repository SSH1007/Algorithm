import sys
input = sys.stdin.readline
N = int(input().rstrip())
dap = 0
for _ in range(N):
    H, B, K = map(int, input().rstrip().split())
    dap += ((0 if H-B>=0 else abs(H-B)) * K)
print(dap)
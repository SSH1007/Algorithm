A, B = map(int, input().split())
N = int(input())
dap = abs(B-A)
for _ in range(N):
    hz = int(input())
    dap = min(dap, abs(hz-B)+1)
print(dap)
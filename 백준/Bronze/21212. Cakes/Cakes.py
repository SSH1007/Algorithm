N = int(input())
dap = 10000
for _ in range(N):
    a, b = map(int, input().split())
    dap = min(dap, b//a)
print(dap)
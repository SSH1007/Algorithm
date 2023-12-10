N = int(input())
dap = 0
for _ in range(N):
    C, K = map(int, input().split())
    dap += C*K
print(dap)
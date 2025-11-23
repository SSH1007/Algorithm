N = int(input())
dap = 0
lst = [int(input()) for _ in range(N)]
M = int(input())
for _ in range(M):
    dap += lst[int(input())-1]
print(dap)
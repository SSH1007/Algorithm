N = int(input())
dap = 0
for _ in range(N):
    a,b = map(int,input().split())
    dap+=(b%a)
print(dap)
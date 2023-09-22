n = int(input())
dap = 0
for _ in range(n):
    q, y = map(float, input().split())
    dap += q*y
print('%.3f'%dap)
year = int(''.join(input().split('-')))
N = int(input())
dap = 0
for _ in range(N):
    limit = int(''.join(input().split('-')))
    if limit >= year:
        dap += 1
print(dap)
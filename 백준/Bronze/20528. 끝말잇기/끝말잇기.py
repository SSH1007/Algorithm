N = int(input())
pal = list(input().split())
pal.sort()
dap = 0
for n in range(N-1):
    if pal[n][-1] != pal[n-1][0]:
        break
else:
    dap = 1
print(dap)
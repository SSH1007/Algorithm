N = int(input())
ass = list(map(int, input().split()))
bss = list(map(int, input().split()))
dap = 0
for n in range(N):
    dap += abs(ass[n]-bss[n])
print(dap//2)
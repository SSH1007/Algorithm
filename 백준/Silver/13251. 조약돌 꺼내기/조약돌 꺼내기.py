M = int(input())
stone = list(map(int, input().split()))
K = int(input())
hap = sum(stone)
dap = 0
for s in stone:
    tmp = 1
    for k in range(K):
       tmp *= (s-k)/(hap-k)
    dap += tmp
print(dap)
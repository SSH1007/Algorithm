N, K, P = map(int, input().split())
cream = list(map(int, input().split()))
dap = 0
for i in range(0, N*K, K):
    bag = cream[i:i+K]
    if bag.count(0) < P:
        dap += 1
print(dap)
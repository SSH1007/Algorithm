ABC = list(map(int,input().split()))
cockA = []
cockB = []
for a in ABC:
    if a%2:
        cockA.append(a)
    else:
        cockB.append(a)
dap = 1
if cockA:
    for c in cockA:
        dap *= c
else:
    for c in cockB:
        dap *= c
print(dap)
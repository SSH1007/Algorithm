S = input()
n = int(input())
dap = 0
for _ in range(n):
    SS = input()
    i = SS.find(S[0])
    SS = SS[i:] + SS[:i]
    if S in SS:
        dap += 1
print(dap)
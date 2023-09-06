N = int(input())
S = input()
dap = 0
S1 = S[:N//2]
S2 = S[N//2:][::-1]
I = min(len(S1), len(S2))
for i in range(I):
    if S1[i] != S2[i]:
        dap += 1
print(dap)
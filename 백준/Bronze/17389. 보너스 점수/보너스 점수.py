N = int(input())
S = input()
bonus = 0
dap = 0
for n in range(N):
    if S[n] == 'O':
        dap+=(n+1)
        dap+=bonus
        bonus+=1
    else:
        bonus = 0
print(dap)
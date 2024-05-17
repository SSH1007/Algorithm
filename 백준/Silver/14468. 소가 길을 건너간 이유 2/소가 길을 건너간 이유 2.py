cows = input()
dap = 0
for i in range(52):
    for j in range(i+1, 52):
        if cows[i] == cows[j]:
            for c in cows[i:j+1]:
                if cows[i:j+1].count(c) == 1:
                    dap += 1
print(dap//2)
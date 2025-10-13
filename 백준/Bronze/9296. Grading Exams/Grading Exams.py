T = int(input())
for t in range(1, T+1):
    L = int(input())
    a = input()
    b = input()
    dap = 0
    for l in range(L):
        if a[l] != b[l]:
            dap += 1
    print(f'Case {t}: {dap}')
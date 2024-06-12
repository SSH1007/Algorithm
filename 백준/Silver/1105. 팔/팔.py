L, R = input().split()
if len(L) < len(R):
    print(0)
else:
    dap = 0
    for i in range(len(L)):
        if L[i] == '8' and R[i] == '8':
            dap += 1
        elif L[i] == R[i]:
            continue
        else:
            break
    print(dap)
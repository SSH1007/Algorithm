K = int(input())
cipher = input()
l = len(cipher)
dap = ['' for _ in range(l)]
cnt = 0
for i in range(0, l, K):
    if cnt%2:
        for j in range(K):
            dap[cnt+j*(l//K)] = cipher[i:i+K][::-1][j]
    else:
        for j in range(K):
            dap[cnt+j*(l//K)] = cipher[i:i+K][j]
    cnt += 1
print(''.join(dap))
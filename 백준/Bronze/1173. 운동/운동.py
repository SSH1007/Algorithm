N, m, M, T, R = map(int, input().split())
cur_m = m
dap = 0
if m + T > M:
    dap = -1
else:
    while N > 0:
        if cur_m + T <= M:
            cur_m += T
            dap += 1
            N -= 1
        else:
            cur_m -= R
            if cur_m < m:
                cur_m = m
            dap += 1
print(dap)
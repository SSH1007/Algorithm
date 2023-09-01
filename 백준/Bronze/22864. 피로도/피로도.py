A, B, C, M = map(int, input().split())
time = 0
piro = 0
dap = 0

while piro <= M:
    if piro + A > M:
        time += 1
        piro = max(0, piro-C)

    else:
        piro += A
        dap += B
        time += 1
    if time == 24:
        break
print(dap)
N, a, b = map(int, input().split())
dap = 0
for _ in range(N):
    house, *lst = map(int, input().split())
    for l in lst:
        tmp = 0
        tmp += bin(l)[2:].count('1')*b
        tmp += bin(l)[2:].count('0')*a
        dap += tmp
print(dap)
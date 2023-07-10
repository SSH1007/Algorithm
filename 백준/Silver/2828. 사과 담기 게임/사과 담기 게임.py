N, M = map(int, input().split())
J = int(input())
s, e = 1, M
dap = 0
for _ in range(J):
    idx = int(input())
    while 1:
        if s <= idx <= e:
            break
        elif idx > e:
            s += 1
            e += 1
        elif idx < s:
            s -= 1
            e -= 1
        dap += 1
print(dap)
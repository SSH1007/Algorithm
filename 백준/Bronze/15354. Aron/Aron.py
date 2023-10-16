T = int(input())
former = ''
dap = 1
for _ in range(T):
    t = input()
    if former != t:
        dap += 1
        former = t
print(dap)
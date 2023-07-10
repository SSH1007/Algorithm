def GCD(a, b):
    while b != 0:
        a, b = b, a % b
    return a

t = int(input())
for _ in range(t):
    dap = 0
    lst = list(map(int, input().split()))
    for i in range(1, lst[0]):
        for j in range(i + 1, lst[0]+1):
            dap += GCD(lst[i], lst[j])
    print(dap)
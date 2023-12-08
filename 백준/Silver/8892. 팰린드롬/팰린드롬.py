def f():
    k = int(input())
    lst = [input() for _ in range(k)]
    for i in range(len(lst)):
        for j in range(len(lst)):
            if i!=j:
                if lst[i]+lst[j] == lst[j][::-1]+lst[i][::-1]:
                    return lst[i]+lst[j]
    return 0

T = int(input())
for _ in range(T):
    dap = f()
    print(dap if dap != 0 else 0)
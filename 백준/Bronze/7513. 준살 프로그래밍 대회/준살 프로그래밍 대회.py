for t in range(1, int(input())+1):
    if t != 1:
        print()
    m = int(input())
    lst = []
    for _ in range(m):
        lst.append(input())
    print(f'Scenario #{t}:')
    n = int(input())
    for _ in range(n):
        dap = ''
        k, *idx = map(int, input().split())
        for i in idx:
            dap += lst[i]
        print(dap)
T = int(input())
for t in range(1, T+1):
    lst = list(map(int, input().split()))
    print('Case %d: %d' % (t, lst[0]-1), end=' ')
    dap = []
    i = lst[0]
    for n in range(1, len(lst)-1):
        dap.append(lst[n]*i)
        i -= 1
    print(*dap)
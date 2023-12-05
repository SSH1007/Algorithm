N, M = map(int, input().split())
dap = []
if N > 0:
    lst = list(map(int, input().split()))
    tmp = []
    for i in range(N):
        tmp.append(lst[i])
        if sum(tmp) > M:
            a = tmp.pop()
            dap.append(tmp)
            tmp = [a]
    dap.append(tmp)
print(len(dap))
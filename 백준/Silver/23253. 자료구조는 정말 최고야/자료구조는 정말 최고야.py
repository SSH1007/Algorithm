dap = 'Yes'
N, M = map(int,input().split())
for _ in range(M):
    _ = int(input())
    lst = list(map(int, input().split()))
    if dap == 'Yes':
        while len(lst) > 1:
            p = lst.pop()
            if lst[-1] < p:
                dap = 'No'
                break
    else:
        break
print(dap)
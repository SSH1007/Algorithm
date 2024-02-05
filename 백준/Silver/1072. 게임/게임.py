X, Y = map(int, input().split())
Z = int(Y*100//X)
s, e = 0, X
dap = 0
if Z >= 99:
    print(-1)
else:
    while s <= e:
        mid = (s+e)//2
        if int((Y+mid)*100//(X+mid)) <= Z:
            dap = mid
            s = mid + 1
        else:
            e = mid - 1
    print(dap+1)
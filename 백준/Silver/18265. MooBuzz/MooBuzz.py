def check(mid):
    three = mid//3
    five = mid//5
    fifteen = mid//15
    return mid - (three + five - fifteen)


N = int(input())
s, e = 1, N*10
dap = 0
while s <= e:
    mid = (s+e)//2
    if check(mid) >= N:
        dap = mid
        e = mid-1
    else:
        s = mid+1
print(dap)
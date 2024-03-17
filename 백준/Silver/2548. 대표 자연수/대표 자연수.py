N = int(input())
lst = sorted(list(map(int, input().split())))
s, e = 0, N
dap = int(1e9)
maxV = sum(lst)
while s <= e:
    mid = (s+e)//2
    hap = sum([abs(l-lst[mid]) for l in lst])
    if hap <= maxV:
        dap = min(dap, lst[mid])
        maxV = hap
        e = mid-1
    else:
        s = mid+1
print(dap)
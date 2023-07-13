N = int(input())
lst = list(map(int, input().split()))
X = int(input())
lst.sort()
s, e = 0, N-1
dap = 0
while s < e:
    if lst[s]+lst[e] < X:
        s+=1
    elif lst[s]+lst[e] > X:
        e-=1
    else:
        dap += 1
        s += 1
print(dap)
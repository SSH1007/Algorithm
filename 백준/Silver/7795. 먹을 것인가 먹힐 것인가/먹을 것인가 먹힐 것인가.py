T = int(input())
for _ in range(T):
    N, M = map(int, input().split())
    As = list(map(int, input().split()))
    Bs = list(map(int, input().split()))
    As.sort()
    Bs.sort()
    dap = 0
    for i in range(N):
        s, e = 0, M-1
        while s <= e:
            mid = (s+e)//2
            if Bs[mid] >= As[i]:
                e = mid-1
            elif Bs[mid] < As[i]:
                s = mid+1
        dap += s
    print(dap)
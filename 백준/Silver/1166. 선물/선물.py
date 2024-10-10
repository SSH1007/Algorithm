def check(mid):
    global N, L, W, H
    a = L//mid
    b = W//mid
    c = H//mid
    return a*b*c >= N


N, L, W, H = map(int, input().split())
s, e = 0, max(L, W, H)
dap = 0.0
cnt = 10000
while s <= e and cnt > 0:
    mid = (s+e)/2
    if check(mid):
        dap = max(dap, mid)
        s = mid
    else:
        e = mid
    cnt -= 1
print(dap)
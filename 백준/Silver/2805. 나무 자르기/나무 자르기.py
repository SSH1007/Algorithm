# 이분 탐색 문제
N, M = map(int, input().split())
trees = list(map(int, input().split()))
s,e = 1, max(trees)
while s <= e:
    mid = (s+e)//2
    dap = 0
    for t in trees:
        if t > mid:
            dap += (t-mid)
    if dap >= M:
        s = mid+1
    elif dap < M:
        e = mid-1
print(e)
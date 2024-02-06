def merge_sort(A, p, r):
    if p < r:
        q = (p+r)//2
        merge_sort(A, p, q)
        merge_sort(A, q+1, r)
        merge(A, p, q, r)


def merge(A, p, q, r):
    global cnt, dap
    i = p
    j = q+1
    tmp = []
    while i <= q and j <= r:
        if A[i] <= A[j]:
            tmp.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            j += 1
    while i <= q:
        tmp.append(A[i])
        i += 1
    while j <= r:
        tmp.append(A[j])
        j += 1
    i = p
    t = 0
    while i <= r:
        cnt += 1
        if cnt == K:
            dap = tmp[t]
        A[i] = tmp[t]
        i += 1
        t += 1


N, K = map(int, input().split())
As = list(map(int, input().split()))
cnt, dap = 0, 0
merge_sort(As, 0, N-1)
if dap:
    print(dap)
else:
    print(-1)
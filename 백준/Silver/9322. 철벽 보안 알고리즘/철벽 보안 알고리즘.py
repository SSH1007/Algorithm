T = int(input())
for _ in range(T):
    N = int(input())
    first = list(input().split())
    second = list(input().split())
    cipher = list(input().split())
    dic = dict()
    for n in range(N):
        dic[n] = first.index(second[n])
    dap = ['' for _ in range(N)]
    for n in range(N):
        dap[dic[n]] = cipher[n]
    print(' '.join(dap))
def I(R, G, B):
    return 2126*R+7152*G+722*B
N, M = map(int, input().split())
dap = []
for _ in range(N):
    art = ''
    lst = list(map(int, input().split()))
    for i in range(0, 3*M, 3):
        tmp = I(lst[i], lst[i+1], lst[i+2])
        if 0 <= tmp < 510000:
            art += '#'
        elif 510000 <= tmp < 1020000:
            art += 'o'
        elif 1020000 <= tmp < 1530000:
            art += '+'
        elif 1530000 <= tmp < 2040000:
            art += '-'
        else:
            art += '.'
    dap.append(art)
for d in dap:
    print(d)
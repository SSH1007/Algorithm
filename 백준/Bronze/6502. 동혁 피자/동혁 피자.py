cnt = 0
while 1:
    cnt += 1
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    r, w, l = lst[0], lst[1], lst[2]
    if (w**2+l**2)**0.5 > 2*r:
        print(f'Pizza {cnt} does not fit on the table.')
    else:
        print(f'Pizza {cnt} fits on the table.')
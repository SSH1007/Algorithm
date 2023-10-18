abc = 'abcdefghijklmnopqrstuvwxyz'
T = int(input())
for _ in range(T):
    txt = sorted(list(set(input().lower())))
    lst = []
    for a in abc:
        if a not in txt:
            lst.append(a)
    if not lst:
        print('pangram')
    else:
        print('missing', end=' ')
        print(''.join(lst))
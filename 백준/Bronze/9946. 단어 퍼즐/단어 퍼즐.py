cnt = 1
while 1:
    a = sorted(input())
    b = sorted(input())
    if ''.join(a) == 'DEN' and a == b:
        break
    if a == b:
        print('Case %d: same'%cnt)
    else:
        print('Case %d: different'%cnt)
    cnt += 1
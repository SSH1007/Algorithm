for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())

    if p1<x2 or y1>q2 or x1>p2 or q1<y2:
        print('d')
        continue
    elif p1==x2 or p2==x1:
        if q1==y2 or y1==q2:
            print('c')
            continue
        else:
            print('b')
            continue
    elif q1==y2 or y1==q2:
        print('b')
        continue
    else:
        print('a')
while 1:
    N = int(input())
    if N == 0:
        break
    lst = []
    maxv = 0
    maxcnt = 0
    for n in range(N):
        a, b = input().split()
        b = float(b)
        if maxv < b:
            maxv = b
            maxcnt = 1
        elif maxv == b:
            maxcnt += 1

        lst.append((a, b, n))
    lst.sort(key=lambda x:(-x[1], x[2]))
    for d in lst[:maxcnt]:
        print(d[0], end = ' ')
    print()
while 1:
    N = int(input())
    if N:
        lst = list(map(int, input().split()))
        mc = lst.count(0)
        jc = lst.count(1)
        print('Mary won %d times and John won %d times' % (mc, jc))
        continue
    break
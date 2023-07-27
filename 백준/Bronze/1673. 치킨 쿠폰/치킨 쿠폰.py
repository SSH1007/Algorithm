while 1:
    try:
        n, k = map(int, input().split())
        ate = 0
        stamp = 0
        while n > 0:
            ate += n
            stamp += n
            n = 0
            n += (stamp//k)
            stamp %= k
        print(ate)
    except EOFError:
        break
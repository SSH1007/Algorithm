while 1:
    try:
        n = int(input())
        if n == 1:
            print(1)
        else:
            k = 11
            while 1:
                if k % n == 0:
                    break
                else:
                    k = k*10+1
            print(len(str(k)))
    except:
        break
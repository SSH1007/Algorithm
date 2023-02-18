while 1:
    f, s = map(int, input().split())
    if f==0 and s==0:
        break
    n = f-s
    if n%2:
        if n>=3:
            print((n-3)//2, 1)
        else:
            print(0,0)
    else:
        print(n//2,0) 
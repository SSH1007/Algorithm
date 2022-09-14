for _ in range(int(input())):
    A,B = map(int,input().split())
    while 1:
        if A>B:
            A//=2
        elif A<B:
            B//=2
        else:
            print(B*10)
            break
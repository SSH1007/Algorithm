for _ in range(int(input())):
    A,B = map(int,input().split())
    arr = []
    while A>0:
        arr.append(A)
        A//=2
    while B>0:
        if B in arr:
            break
        B//=2
    print(B*10)
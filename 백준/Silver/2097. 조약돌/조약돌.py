N = int(input())
if N < 3:
    print(4)
else:
    n = round(N**0.5)
    if n**2 >= N:
        print((n-1)*4)
    else:
        print((n-1)*2+n*2)
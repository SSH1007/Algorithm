def ga(p, w):
    don = 0
    if 10*p >= 5000:
        don = 10*p-500
    else:
        don = 10*p
    return (10*w) / don

Sp, Sw = map(int, input().split())
Np, Nw = map(int, input().split())
Up, Uw = map(int, input().split())
Sg = ga(Sp, Sw)
Ng = ga(Np, Nw)
Ug = ga(Up, Uw)
if Sg == max((Sg, Ng, Ug)):
    print('S')
elif Ng == max((Sg, Ng, Ug)):
    print('N')
else:
    print('U')
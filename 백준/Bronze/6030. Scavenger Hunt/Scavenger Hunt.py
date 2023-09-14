def y(n):
    lst = []
    for i in range(1, n+1):
        if n%i == 0:
            lst.append(i)
    return lst


P, Q = map(int, input().split())
plst = y(P)
qlst = y(Q)
for p in plst:
    for q in qlst:
        print(p, q)
N, L = map(int, input().split())

while 1:
    iterL = L

    lst = list(range(iterL))
    minus = sum(lst)

    newN = N
    newN-=minus
    if L>100 or newN<0:
        print(-1)
        break
    elif newN == 0 or newN%L==0:
        print(*list(range(newN//L,newN//L+lst[-1]+1)))
        break
    L+=1
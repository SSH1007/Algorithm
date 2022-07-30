while 1:
    lst = list(map(int,input().split()))
    if lst == [0,0,0]:
        break
    if lst[2]-lst[1] == lst[1]-lst[0]:
        print('AP',lst[2]*2-lst[1])
    elif lst[2]//lst[1] == lst[1]//lst[0]:
        print('GP',(lst[2]**2)//lst[1])
n = 1
while 1:
    lst = list(map(int, input().split()))
    if lst[0] == 0:
        break
    if lst[0]%2:
        print(f'Case {n}: {lst[(lst[0]+1)//2]:.1f}')
    else:
        print(f'Case {n}: {(lst[lst[0]//2]+lst[(lst[0])//2+1])/2:.1f}')
    n+=1
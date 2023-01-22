groupN = 1
while 1:
    nastyCnt = 0
    if groupN != 1:
        print()
    N = int(input())
    if N == 0:
        break
    group = []
    for n in range(N):
        group.append(list(input().split()))
    print(f'Group {groupN}')
    for i in range(len(group)):
        for j in range(1,len(group[i])):
            if group[i][j] == 'N':
                print(f'{group[(i+1-j)%N-1][0]} was nasty about {group[i][0]}')
                nastyCnt+=1
    if nastyCnt == 0:
        print('Nobody was nasty')    
    groupN+=1
n = int(input())
for i in range(n):
    players = list(map(int, input().split()))
    if i !=0:
        print() 
    if 17 in players and 18 in players:
        print(*players)
        print('both')
    elif 17 in players:
        print(*players)
        print('zack')
    elif 18 in players:
        print(*players)
        print('mack')
    else:
        print(*players)
        print('none')
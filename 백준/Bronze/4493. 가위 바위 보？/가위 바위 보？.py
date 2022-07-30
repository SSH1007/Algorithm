import sys
input = sys.stdin.readline
t = int(input())
for _ in range(t):
    n = int(input())
    acnt,bcnt =0,0
    for _ in range(n):
        a,b=input().split()
        if (a == 'R' and b =='S') or (a =='S' and b == 'P') or (a == 'P' and b =='R'):
            acnt+=1
        elif (b == 'R' and a =='S') or (b =='S' and a == 'P') or (b == 'P' and a =='R'):
            bcnt+=1
    if acnt>bcnt:
        print('Player 1')
    elif acnt<bcnt:
        print('Player 2')
    else:
        print('TIE')
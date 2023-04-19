import sys
input = sys.stdin.readline
cnt = 1
while 1:
    N = int(input().rstrip())
    if N == 0:
        break
    print(f'{cnt}. ',end='')
    n1 = 3*N
    if n1%2:
        print('odd', end = ' ')
        n2 = (n1+1)//2
    else:
        print('even', end = ' ')
        n2 = n1//2
    n3 = 3*n2
    n4 = n3//9
    print(n4)
    cnt+=1
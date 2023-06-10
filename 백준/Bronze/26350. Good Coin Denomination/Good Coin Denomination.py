import sys
input = sys.stdin.readline
n = int(input().rstrip())
for i in range(n):
    lst = list(map(int, input().rstrip().split()))
    if i != 0:
        print()
    flag = True
    for i in range(2,len(lst)):
        if not lst[i] >= lst[i-1]*2:
            flag = False
    print('Denominations: ', end='')
    for i in range(1,len(lst)):
        print(lst[i], end = ' ')
    print()
    if flag:
        print('Good coin denominations!')
    else:
        print('Bad coin denominations!')
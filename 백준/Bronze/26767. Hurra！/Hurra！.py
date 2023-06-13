import sys
input = sys.stdin.readline
N = int(input().rstrip())
for n in range(1, N+1):
    if n%7==0 and n%11!=0:
        print('Hurra!')
    elif n%7!=0 and n%11==0:
        print('Super!')
    elif n%7==0 and n%11==0:
        print('Wiwat!')
    else:
        print(n)
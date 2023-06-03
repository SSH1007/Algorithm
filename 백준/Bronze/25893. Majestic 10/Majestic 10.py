import sys
input = sys.stdin.readline
N = int(input().rstrip())
for n in range(N):
    if n!=0:
        print()
    a, b, c = map(int, input().rstrip().split())
    print(a,b,c)
    if a>=10 and b>=10 and c>= 10:
        print('triple-double')
    elif a<10 and b<10 and c<10:
        print('zilch')
    elif (a>=10 and b>=10) or (a>=10 and c>=10) or (b>=10 and c>=10):
        print('double-double')
    elif a>=10 or b>=10 or c>=10:
        print('double')
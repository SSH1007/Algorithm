import sys
input = sys.stdin.readline
H1, B1 = map(int, input().rstrip().split())
H2, B2 = map(int, input().rstrip().split())
a1 = H1*3+B1
a2 = H2*3+B2
if a1>a2:
    print(1, a1-a2)
elif a1<a2:
    print(2, a2-a1)
else:
    print('NO SCORE')
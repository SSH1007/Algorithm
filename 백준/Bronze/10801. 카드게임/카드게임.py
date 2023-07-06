import sys
input = sys.stdin.readline
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
Acnt, Bcnt = 0, 0
for i in range(10):
    if A[i] > B[i]:
        Acnt+=1
    elif A[i] < B[i]:
        Bcnt+=1
if Acnt > Bcnt:
    print('A')
elif Acnt < Bcnt:
    print('B')
else:
    print('D')
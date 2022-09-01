import math
A,P1 = map(int,input().split())
R,P2 = map(int,input().split())
B = R*R*math.pi

if A/P1 > B/P2:
    print('Slice of pizza')
else:
    print('Whole pizza')
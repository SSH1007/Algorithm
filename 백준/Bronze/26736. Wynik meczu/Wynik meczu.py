import sys
input =  sys.stdin.readline
S = input().rstrip()
A, B = 0, 0
for s in S:
    if s =='A':
        A+=1
    else:
        B+=1
print(f'{A} : {B}')
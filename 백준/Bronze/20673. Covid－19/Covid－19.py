import sys
input = sys.stdin.readline
p = int(input().rstrip())
q = int(input().rstrip())
if p<=50 and q<=10:
    print('White')
elif q>30:
    print('Red')
else:
    print('Yellow')
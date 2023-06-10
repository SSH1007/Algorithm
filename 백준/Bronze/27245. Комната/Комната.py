import sys
input = sys.stdin.readline
w = int(input().rstrip())
l = int(input().rstrip())
h = int(input().rstrip())
if min(w,l)/h >= 2 and not max(w,l)/min(w,l)>2:
    print('good')
else:
    print('bad')
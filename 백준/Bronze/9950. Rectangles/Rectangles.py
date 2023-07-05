import sys
input = sys.stdin.readline

while 1:
    l, w, a = map(int, input().rstrip().split())
    if l==w and w==a and a==0:
        break
    if l==0:
        print(a//w, w, a)
    elif w==0:
        print(l, a//l, a)
    elif a==0:
        print(l, w, l*w)
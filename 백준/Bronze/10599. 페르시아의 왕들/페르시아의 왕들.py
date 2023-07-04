import sys
input = sys.stdin.readline
while 1:
    a, b, c, d = map(int, input().rstrip().split())
    if a==b and b==c and c==d and d==0:
        break
    print(c-b, d-a)
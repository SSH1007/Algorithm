import sys
input = sys.stdin.readline
x1, y1 = map(int, input().rstrip().split())
x2, y2 = map(int, input().rstrip().split())
x3, y3 = map(int, input().rstrip().split())
tmp = (x2*y3)-(x1*y3)-(x2*y1)-(x3*y2)+(x3*y1)+(x1*y2)
if tmp > 0:
    print(1)
elif tmp == 0:
    print(0)
else:
    print(-1)
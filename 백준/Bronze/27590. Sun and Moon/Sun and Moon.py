import sys
input = sys.stdin.readline
ds, ys = map(int, input().rstrip().split())
dm, ym, = map(int, input().rstrip().split())

s = -1 * ds
m = -1 * dm
while 1:
    if s>m:
        m+=ym
    elif s<m:
        s+=ys
    else:
        break
print(s)
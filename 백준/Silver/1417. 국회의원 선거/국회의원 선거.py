import sys
input = sys.stdin.readline

N = int(input().rstrip())
me = int(input().rstrip())
other = []
for _ in range(N-1):
    other.append(int(input().rstrip()))
preMe = me
if other:
    while 1:
        if me > max(other):
            break
        for i in range(N-1):
            if other[i] >= me and other[i] == max(other):
                other[i] -= 1
                me += 1
    print(me - preMe)
else:
    print(0)
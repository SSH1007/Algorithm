import sys
input = sys.stdin.readline
M = int(input().rstrip())
# cw=0: 시계방향, cw=1: 반시계방향
cw, rpm = 0, 1
for _ in range(M):
    a, b, s = map(int, input().rstrip().split())
    rpm = (rpm*b)//a
    cw = abs(cw-s)

print(cw, rpm)
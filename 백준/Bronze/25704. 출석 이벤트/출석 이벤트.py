import sys
input = sys.stdin.readline
N = int(input().rstrip())
P = int(input().rstrip())
dis = 0
if N >= 20:
    dis = max(500, int(P*0.1), 2000, int(P*0.25))
elif N>=15:
    dis = max(500, int(P*0.1), 2000)
elif N>=10:
    dis = max(500, int(P*0.1))
elif N>=5:
    dis = 500
if dis > P:
    print(0)
else:
    print(P-dis)
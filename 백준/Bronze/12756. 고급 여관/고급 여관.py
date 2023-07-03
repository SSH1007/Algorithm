import sys
input = sys.stdin.readline
import math
atkA, hpA = map(int, input().rstrip().split())
atkB, hpB = map(int, input().rstrip().split())
if math.ceil(hpB/atkA) < math.ceil(hpA/atkB):
    print('PLAYER A')
elif math.ceil(hpB/atkA) > math.ceil(hpA/atkB):
    print('PLAYER B')
else:
    print('DRAW')
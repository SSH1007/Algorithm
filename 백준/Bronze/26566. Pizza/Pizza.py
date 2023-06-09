import sys
import math
input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    A1, P1 = map(int, input().rstrip().split())
    R1, P2 = map(int, input().rstrip().split())
    if A1/P1 > (R1*R1*math.pi)/P2:
        print('Slice of pizza')
    else:
        print('Whole pizza')
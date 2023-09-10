import sys
input = sys.stdin.readline
N = int(input().rstrip())
As = list(map(int, input().rstrip().split()))
V = 0
for a in As:
    V = 1-(1-V/100)*(1-a/100)
    V *= 100
    print(V)
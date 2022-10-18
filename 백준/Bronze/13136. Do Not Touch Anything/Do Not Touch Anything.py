import sys
input = sys.stdin.readline

R, C, N = map(int, input().split())
if R%N:
    R = R//N+1
else:
    R = R//N
if C%N:
    C = C//N+1
else:
    C = C//N
print(R*C)
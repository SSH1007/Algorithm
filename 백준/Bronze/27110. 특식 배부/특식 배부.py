import sys
input = sys.stdin.readline

N = int(input().rstrip())
A, B, C = map(int, input().rstrip().split())
if A>N:
    A=N
if B>N:
    B=N
if C>N:
    C=N
print(A+B+C)
import sys
input = sys.stdin.readline
A, B = map(int, input().rstrip().split())
if A<=B:
    print(B-A)
else:
    print(A+B)
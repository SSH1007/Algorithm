import sys
input = sys.stdin.readline
n, k, a, b = map(int, input().rstrip().split())
A = (n-1)*a
B = (k-1)*b+(n-1)*b
print(B, A)
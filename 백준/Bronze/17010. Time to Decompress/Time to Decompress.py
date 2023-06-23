import sys
input = sys.stdin.readline
L = int(input().rstrip())
for _ in range(L):
    a, b = input().rstrip().split()
    print(b*int(a))
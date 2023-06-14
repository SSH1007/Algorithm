import sys
input = sys.stdin.readline
n = int(input().rstrip())
for _ in range(n):
    a, b = map(float, input().rstrip().split())
    print(round(abs(a-b),1))
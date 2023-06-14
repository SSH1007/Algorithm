import sys
input = sys.stdin.readline
n, m = map(int, input().rstrip().split())
n -= 7
m += 7
if n>0:
    print(n)
else:
    print(m)
import sys
input = sys.stdin.readline
a, b = map(int, input().rstrip().split())
print(b if a>=b else a+1)
import sys
input = sys.stdin.readline
w, h = map(int, input().rstrip().split())
print((w+h)-((w**2+h**2)**0.5))
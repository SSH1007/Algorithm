import sys
input = sys.stdin.readline
n = int(input().rstrip())
start = int(input().rstrip())
for _ in range(2, n+1):
    start += int(input().rstrip())
print(start)
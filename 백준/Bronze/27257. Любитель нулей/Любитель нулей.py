import sys
input = sys.stdin.readline
n = int(input().rstrip()[::-1])
print(str(n).count('0'))
import sys
input = sys.stdin.readline
a = int(input().rstrip())
n = 100/a
m = 100/(100-a)
print(n, m, sep='\n')
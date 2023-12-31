import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = [float(input()) for _ in range(N)]
for i in range(1, N):
    lst[i] = max(lst[i-1]*lst[i], lst[i])
print('%.3f'%max(lst))
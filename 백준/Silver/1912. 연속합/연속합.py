import sys
input = sys.stdin.readline
n = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
for i in range(1, n):
    lst[i] = max(lst[i], lst[i-1]+lst[i])
print(max(lst))
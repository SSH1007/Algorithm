import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = sorted(list(map(int, input().rstrip().split())))
l = (N-1)//2
print(lst[l])
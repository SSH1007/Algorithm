import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = [0] * N
for n in range(N):
    lst[n] = int(input().rstrip())
for l in sorted(lst, reverse=True):
    print(l)
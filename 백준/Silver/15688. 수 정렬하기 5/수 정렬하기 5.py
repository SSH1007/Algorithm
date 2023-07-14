import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
for _ in range(N):
    lst.append(int(input().rstrip()))
for l in sorted(lst):
    print(l)
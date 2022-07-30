import sys
input = sys.stdin.readline
N = int(input())
lst = []
for _ in range(N):
    n = input().rstrip()
    n = n[0].upper() + n[1:]
    lst.append(n)
for l in lst:
    print(l)
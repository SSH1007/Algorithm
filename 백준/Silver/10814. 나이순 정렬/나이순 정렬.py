import sys
input = sys.stdin.readline
N = int(input())
arr = []
for n in range(N):
    lst = input().split()
    arr.append(lst)
arr.sort(key=lambda x : int(x[0]))
for a in arr:
    print(a[0],a[1])
import sys
input =  sys.stdin.readline
N = int(input())
lst = list(map(int, input().split()))
big, small = 0, 1001
for l in lst:
    if l>big:
        big = l
    if l<small:
        small = l
print(big-small)    
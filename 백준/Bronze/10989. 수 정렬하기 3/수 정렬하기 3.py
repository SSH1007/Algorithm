import sys
input=sys.stdin.readline
N=int(input())
lst=[0]*10001
for n in range(N):
    lst[int(input())]+=1
for l in range(10001):
    if lst[l]!=0:
        for j in range(lst[l]):
            print(l)
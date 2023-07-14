import sys
input = sys.stdin.readline
N, P = map(int, input().rstrip().split())
lst = []
cycle = []
start = N
# 더 이상 사이클이 늘어나지 않을때 멈춰야 한다.
while 1:
    start *= N
    start %= P
    length = len(lst)
    cycleL = len(cycle)
    if start not in lst:
        lst.append(start)
    if length == len(lst):
        if start not in cycle:
            cycle.append(start)
        if cycleL == len(cycle):
            break

print(len(cycle))
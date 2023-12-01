import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
for _ in range(N):
    lst.append(float(input().rstrip()))
    if len(lst) > 7:
        lst.sort()
        lst.pop()
for l in lst:
    print(f'{l:.3f}')
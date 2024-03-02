import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = sorted(list(map(float, input().rstrip().split())))
for i in range(N-1):
    lst[N-1] = lst[i]/2+lst[N-1]
print(lst[-1])
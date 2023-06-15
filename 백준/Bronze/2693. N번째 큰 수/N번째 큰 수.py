import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    lst = list(map(int, input().rstrip().split()))
    lst.sort()
    print(lst[7])
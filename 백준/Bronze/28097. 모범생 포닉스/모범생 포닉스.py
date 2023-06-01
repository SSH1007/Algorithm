import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = list(map(int, input().rstrip().split()))
day = sum(lst)+(len(lst)-1)*8
print(day//24, day%24)
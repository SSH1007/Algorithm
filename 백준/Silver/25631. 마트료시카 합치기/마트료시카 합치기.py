import sys
input = lambda: sys.stdin.readline().rstrip()

N = int(input())
As = list(map(int, input().split()))
cnt = 0
while len(As) > 0:
    tmp = set(sorted(As))
    for t in tmp:
        del As[As.index(t)]
    cnt += 1
print(cnt)
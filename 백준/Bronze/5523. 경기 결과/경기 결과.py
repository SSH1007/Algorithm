import sys
input = sys.stdin.readline
N = int(input().rstrip())
aCnt, bCnt = 0, 0
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    if a>b:
        aCnt+=1
    elif a<b:
        bCnt+=1
print(aCnt, bCnt)
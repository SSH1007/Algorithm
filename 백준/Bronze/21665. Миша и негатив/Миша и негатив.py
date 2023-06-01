import sys
input = sys.stdin.readline
A, B = map(int, input().rstrip().split())
cnt = 0
p1, p2 = [], []
for _ in range(A):
    p1.append(input().rstrip())
input().rstrip()
for _ in range(A):
    p2.append(input().rstrip())

for a in range(A):
    for b in range(B):
        if p1[a][b] == p2[a][b]:
            cnt+=1
print(cnt)
import sys
input = sys.stdin.readline
N = int(input().rstrip())
lst = []
for _ in range(N):
    lst.append('@'*N*5)
for _ in range(N):
    lst.append(' '*N*4+'@'*N)
for _ in range(N):
    lst.append('@'*N*5)
for _ in range(N):
    lst.append('@'*N+' ' * N * 4)
for _ in range(N):
    lst.append('@'*N*5)

for i in range(N*5-1, -1, -1):
    for j in range(N*5):
        print(lst[j][i], end='')
    print()
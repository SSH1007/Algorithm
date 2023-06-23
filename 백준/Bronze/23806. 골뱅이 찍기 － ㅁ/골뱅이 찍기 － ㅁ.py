import sys
input = sys.stdin.readline
N = int(input().rstrip())
for i in range(N):
    print('@'*(N*5))
for i in range(N*3):
    print('@'*N + ' '*(N*3) + '@'*N)
for i in range(N):
    print('@'*(N*5))
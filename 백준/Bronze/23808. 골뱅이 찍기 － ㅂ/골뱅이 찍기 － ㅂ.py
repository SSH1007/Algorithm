import sys
input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(2*N):
    print('@'*N + ' '*3*N + '@'*N)
for _ in range(N):
    print('@'*5*N)
for _ in range(N):
    print('@'*N + ' '*3*N + '@'*N)
for _ in range(N):
    print('@'*5*N)
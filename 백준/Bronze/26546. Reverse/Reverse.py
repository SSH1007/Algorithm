import sys
input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    S, i, j = input().rstrip().split()
    print(S[:int(i)]+S[int(j):])
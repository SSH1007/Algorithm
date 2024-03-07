import sys
input = sys.stdin.readline
N = int(input().rstrip())
A = list(map(int, input().rstrip().split()))
B = list(map(int, input().rstrip().split()))
M = int(input().rstrip())
C = list(map(int, input().rstrip().split()))

lst = []
for i in range(N):
    if not A[i]:
        lst.append(B[i])
dap = C[::-1] + lst
for _ in range(M):
    print(dap.pop(), end = ' ')
import sys
input = sys.stdin.readline
N, Q = map(int, input().rstrip().split())
As = sorted(list(map(int, input().rstrip().split())))
nhap = [0]*(N+1)
nhap[1] = As[0]
for i in range(1, N):
    nhap[i+1] = nhap[i] + As[i]
for _ in range(Q):
    L, R = map(int, input().rstrip().split())
    print(nhap[R]-nhap[L-1])
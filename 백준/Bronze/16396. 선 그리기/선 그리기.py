import sys
input = sys.stdin.readline
N = int(input().rstrip())
tmp = [0]*(10001)
for _ in range(N):
    a, b = map(int, input().rstrip().split())
    for i in range(a, b):
        tmp[i] = 1
print(sum(tmp))
import sys
input =  sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    p, t = map(int, input().rstrip().split())
    print(p - t//7 + t//4)
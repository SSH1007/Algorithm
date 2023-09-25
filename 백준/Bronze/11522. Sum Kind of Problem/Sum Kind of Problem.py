import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    a, b = map(int, input().rstrip().split())
    S1 = b*(b+1)//2
    S2 = b*b
    S3 = b*(b+1)
    print(a, S1, S2, S3)
import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    X = input().rstrip()
    s = set(X)
    print(len(s))
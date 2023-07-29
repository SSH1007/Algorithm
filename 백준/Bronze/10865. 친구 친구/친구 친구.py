import sys
input = sys.stdin.readline
N, M = map(int, input().rstrip().split())
friends = [0]*(N+1)
for _ in range(M):
    a, b = map(int, input().rstrip().split())
    friends[a] += 1
    friends[b] += 1
for f in friends[1:]:
    print(f)
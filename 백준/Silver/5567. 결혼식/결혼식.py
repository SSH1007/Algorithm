import sys
input = sys.stdin.readline
n = int(input().rstrip())
m = int(input().rstrip())
friend = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().rstrip().split())
    friend[a].append(b)
    friend[b].append(a)
s = set(friend[1])
for fri in friend[1]:
    for f in friend[fri]:
        s.add(f)
s.discard(1)
print(len(s))
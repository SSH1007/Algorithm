import sys
input = sys.stdin.readline
N = int(input().rstrip())
se = set()
for _ in range(N):
    s = input().rstrip()
    if s in se or s==s[::-1]:
        print(len(s), s[len(s)//2])
        break
    if s not in se:
        se.add(s)
    if s[::-1] not in se:
        se.add(s[::-1])
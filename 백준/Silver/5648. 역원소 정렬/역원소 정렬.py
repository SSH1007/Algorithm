import sys
input = sys.stdin.read

n, *s = input().split()
for i in range(len(s)):
    s[i] = s[i][::-1]
s = list(map(int, s))
print(*sorted(s), sep = '\n')
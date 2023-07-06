import sys
input = sys.stdin.readline

N = int(input().rstrip())
lst = []
for _ in range(N):
    a, b, c, d = input().rstrip().split()
    lst.append((a, int(b), int(c), int(d)))
lst.sort(key= lambda i: (-i[1], i[2], -i[3], i[0]))
for l in lst:
    print(l[0])
import sys
input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    command = list(input().rstrip())
    L, R = [], []
    for c in command:
        if c == '<':
            if L:
                R.append(L.pop())
        elif c == '>':
            if R:
                L.append(R.pop())
        elif c == '-':
            if L:
                L.pop()
        else:
            L.append(c)
    R = list(reversed(R))
    print(''.join(L+R))
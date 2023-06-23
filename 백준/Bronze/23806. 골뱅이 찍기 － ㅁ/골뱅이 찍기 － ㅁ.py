import sys
input = sys.stdin.readline
N = int(input().rstrip())
for i in range(N):
    for j in range(N*5):
        print('@', end='')
    print()
for i in range(N*3):
    for j in range(N):
        print('@', end='')
    for _ in range(N*3):
        print(' ', end='')
    for j in range(N):
        print('@', end='')
    print()
for i in range(N):
    for j in range(N*5):
        print('@', end='')
    print()
import sys
input = sys.stdin.readline
N = int(input().rstrip())
for _ in range(N):
    x, y = input().rstrip().split()
    print('Distances:', end='')
    for i in range(len(x)):
        d = ord(y[i])-ord(x[i])
        print(f' {26+d if d<0 else d}', end='')
    print()
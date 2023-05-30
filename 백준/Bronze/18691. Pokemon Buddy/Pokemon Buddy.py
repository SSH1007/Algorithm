import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    G, C, E = map(int, input().rstrip().split())
    if G == 1:
        print(max((E-C),0))
    elif G == 2:
        print(max((E-C)*3, 0))
    elif G == 3:
        print(max((E-C)*5, 0))
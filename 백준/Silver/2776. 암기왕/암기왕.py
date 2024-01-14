import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    Nset = set(list(map(int, input().split())))

    M = int(input())
    Mlst = list(map(int, input().split()))
    for l in Mlst:
        if l in Nset:
            print(1)
        else:
            print(0)
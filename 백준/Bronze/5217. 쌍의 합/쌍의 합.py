import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    print(f'Pairs for {N}: ', end='')
    lst = []
    for n in range(1,N):
        for i in range(n+1,N):
            if n+i==N:
                lst.append((n, i))
    for l in range(len(lst)):
        if l>0:
            print(', ', end='')
        print(*lst[l], end='')
    print()
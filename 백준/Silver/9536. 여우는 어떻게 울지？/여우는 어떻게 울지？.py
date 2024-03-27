import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    lst = list(input().rstrip().split())
    while 1:
        Q = list(input().rstrip().split())
        if Q[1] != 'goes':
            print(*lst)
            break
        else:
            while Q[2] in lst:
                lst.remove(Q[2])
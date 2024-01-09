import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    N = int(input())
    first = list(input().rstrip().split())
    second = list(input().rstrip().split())
    cipher = list(input().rstrip().split())
    dic = dict()
    for n in range(N):
        dic[n] = first.index(second[n])
    dap = ['' for _ in range(N)]
    for n in range(N):
        dap[dic[n]] = cipher[n]
    print(' '.join(dap))
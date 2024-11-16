import sys
input = lambda: sys.stdin.readline().rstrip()


N = int(input())
dic = {i: [] for i in range(1, N+1)}
for _ in range(N-1):
    a, b = map(int, input().split())
    dic[a].append(b)
    dic[b].append(a)

Q = int(input())
for _ in range(Q):
    t, k = map(int, input().split())
    if t == 1:
        if len(dic[k]) == 1:
            print('no')
        else:
            print('yes')
    # 단절선은 무조건 yes
    else:
        print('yes')
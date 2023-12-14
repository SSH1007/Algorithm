T = int(input())
for _ in range(T):
    J, N = map(int, input().split())
    lst = []
    for _ in range(N):
        R, C = map(int, input().split())
        lst.append(R*C)
    lst.sort(reverse=True)
    cnt = 0
    while J > 0:
        J -= lst[cnt]
        cnt += 1
    print(cnt)
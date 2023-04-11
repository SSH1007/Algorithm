T = int(input())
for _ in range(T):
    N = int(input())
    lst = [0 for _ in range(N+2)]
    lst[0], lst[1], lst[2] = 1, 1, 1
    for i in range(3,N):
        lst[i] = lst[i-2]+lst[i-3]
    print(lst[N-1])
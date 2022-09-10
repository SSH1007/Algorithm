N, Q = map(int, input().split())
lst = []
for n in range(1,N+1):
    lst += [n]*(int(input()))
for _ in range(Q):
    q = int(input())
    print(lst[q])
import sys
input = sys.stdin.readline
x, N = map(int, input().rstrip().split())
lst = [0]*(N+1)
lst[0] = x
for n in range(1, N+1):
    if lst[n-1]%2:
        lst[n] = (lst[n-1]*2)^6
    else:
        lst[n] = (lst[n-1]//2)^6
print(lst[N])
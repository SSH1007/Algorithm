import sys
input = sys.stdin.readline
S0, N, M = map(int, input().rstrip().split())
lst = [0]*S0
n = 0
for _ in range(N+M):
    command = int(input().rstrip())
    if command:
        if n < S0:
            lst[n] = 1
        else:
            lst = lst[::]+[0]*S0
            lst[n] = 1
            S0 *= 2
        n += 1
    else:
        n -= 1
        lst[n] = 0
print(len(lst))
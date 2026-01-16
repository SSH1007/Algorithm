N = int(input())
t, r = 1, 0
for _ in range(N):
    S, X = input().split()
    n = t
    X = int(X)
    if S == 'HOURGLASS':
        if X != n:
            r ^= 1
        else:
            X = -1
    if r:
        t = (t-2)%12+1
    else:
        t = t%12+1
    if X == n:
        print(n, 'YES')
    else:
        print(n, 'NO')
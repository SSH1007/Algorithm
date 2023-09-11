N, X = map(int, input().split())
Ts = list(map(int, input().split()))
i = 0
while 1:
    if Ts[i] < X:
        print(i+1)
        break
    X += 1
    i += 1
    i %= N
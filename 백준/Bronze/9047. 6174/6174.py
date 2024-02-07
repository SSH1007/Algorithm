T = int(input())
for _ in range(T):
    N = input()
    cnt = 0
    while N != '6174':
        N = list(N)
        if len(N) < 4:
            N += (4-len(N))*['0']
        minN = sorted(N)
        maxN = sorted(N, reverse=True)
        N = str(int(''.join(maxN)) - int(''.join(minN)))
        cnt += 1
    print(cnt)
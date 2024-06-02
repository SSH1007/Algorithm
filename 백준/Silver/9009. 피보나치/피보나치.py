fibo = [0]*45
fibo[0] = 0
fibo[1] = 1
for i in range(2, 45):
    fibo[i] = fibo[i-1] + fibo[i-2]

T = int(input())
for _ in range(T):
    N = int(input())
    tmp = []
    i = 44
    while N:
        if fibo[i] <= N:
            N -= fibo[i]
            tmp.append(fibo[i])
        i -= 1
    print(*tmp[::-1])
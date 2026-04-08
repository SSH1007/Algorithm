N = int(input())
As = list(map(int, input().split()))
f = 0
for n in range(1, N):
    if f == 0 and As[n-1] < As[n]:
        continue
    elif f == 0 and As[n-1] > As[n]:
        f += 1
    elif f == 1 and As[n-1] > As[n]:
        continue
    else:
        print('NO')
        exit(0)
print('YES')
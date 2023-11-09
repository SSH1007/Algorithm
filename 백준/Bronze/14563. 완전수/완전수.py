T = int(input())
lst = list(map(int, input().split()))
for l in lst:
    y = []
    for i in range(1, l):
        if l%i == 0:
            y.append(i)
    std = sum(y)
    if std > l:
        print('Abundant')
    elif std < l:
        print('Deficient')
    else:
        print('Perfect')
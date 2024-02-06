l = (10**6)+1
lst = [1]*l
for i in range(2, l):
    if lst[i]:
        for j in range(i+i, l, i):
            lst[j] = 0
che = []
for i in range(2, l):
    if lst[i]:
        che.append(i)

N = int(input())
for _ in range(N):
    S = int(input())
    for c in che:
        if S%c == 0:
            print('NO')
            break
    else:
        print('YES')
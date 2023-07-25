N = int(input().rstrip())
lst = []
for _ in range(N):
    tmp = list(map(int, input().rstrip().split()))
    lst.append(tmp)

for i in range(3):
    for j in range(N-1):
        tmp = False
        for k in range(j+1, N):
            if lst[j][i] == lst[k][i] and lst[j][i] != 0:
                tmp = True
                lst[k][i] = 0
        if tmp:
            lst[j][i] = 0

for l in lst:
    print(sum(l))
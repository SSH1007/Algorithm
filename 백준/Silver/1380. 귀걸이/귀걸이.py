sn = 1
while 1:
    n = int(input())
    if n == 0:
        break
    name = []
    number = []
    for i in range(n):
        name.append(input())
    for i in range(2*n-1):
        number.append(int(input().split()[0]))
    for n in set(number):
        if number.count(n)==1:
            print(sn, name[n-1])
    sn+=1
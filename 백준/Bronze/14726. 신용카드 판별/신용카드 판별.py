T = int(input())
for _ in range(T):
    number = input()
    lst = []
    for i in range(len(number)):
        if i%2:
            lst.append(int(number[i]))
        else:
            b = 2*int(number[i])
            if b >= 10:
                b = sum(map(int, str(b)))
            lst.append(b)
    hap = sum(lst)
    if hap%10:
        print('F')
    else:
        print('T')
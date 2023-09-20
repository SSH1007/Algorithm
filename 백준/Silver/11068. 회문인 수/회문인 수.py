T = int(input())
for _ in range(T):
    a = int(input())
    for i in range(2, 65):
        lst = []
        b = a
        while b != 0:
            lst.append(b % i)
            b //= i
        if lst == lst[::-1]:
            print(1)
            break
    else:
        print(0)
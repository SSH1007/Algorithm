T = int(input())
for _ in range(T):
    lst = list(map(int, input().split()))
    even = sum([lst[i] for i in range(1, lst[0]+1) if lst[i] % 2 == 0])
    odd = sum([lst[i] for i in range(1, lst[0]+1) if lst[i] % 2])
    if even > odd:
        print('EVEN')
    elif even < odd:
        print('ODD')
    else:
        print('TIE')
N = int(input())
if N == 0:
    print('divide by zero')
else:
    lst = list(map(int, input().split()))
    son = sum(lst)/N
    sat = set(lst)
    mom = 0
    for s in sat:
        mom += s*(lst.count(s)/N)
    if mom == 0:
        print('divide by zero')
    else:
        print(f'{son/mom:.2f}')
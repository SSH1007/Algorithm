K = int(input())
for k in range(1, K+1):
    if k != 1:
        print()
    h = int(input())
    act = input()
    for a in act:
        if a == 'c':
            h += 1
        else:
            h -= 1
    print(f'Data Set {k}:')
    print(h)
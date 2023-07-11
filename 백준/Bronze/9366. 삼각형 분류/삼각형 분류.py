T = int(input())
for t in range(1, T+1):
    a, b, c = map(int, input().split())
    lst = [a, b, c]
    lst.sort()
    S = set((a,b,c))
    if lst[2] >= lst[1]+lst[0]:
        print(f'Case #{t}: invalid!')
    else:
        if len(S) == 1:
            print(f'Case #{t}: equilateral')
        elif len(S) == 2:
            print(f'Case #{t}: isosceles')
        else:
            print(f'Case #{t}: scalene')
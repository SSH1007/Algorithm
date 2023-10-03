T = int(input())
for _ in range(T):
    N = int(input())
    Ws = list(map(int, input().split()))
    if sum(Ws) > 0:
        print('Right')
    elif sum(Ws) < 0:
        print('Left')
    else:
        print('Equilibrium')
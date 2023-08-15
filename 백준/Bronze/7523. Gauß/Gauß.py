T = int(input())
for t in range(1, T+1):
    n, m = map(int, input().split())
    if t != 1:
        print()
    print(f'Scenario #{t}:')
    a = (m-n+1)
    print((m+n)*a//2)
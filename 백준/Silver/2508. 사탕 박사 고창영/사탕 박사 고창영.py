t = int(input())
for _ in range(t):
    _ = input()
    r, c = map(int, input().split())
    lst = [input() for _ in range(r)]

    lst2 = zip(*lst)

    horizon = 0
    for l in lst:
        horizon += ''.join(l).count('>o<')

    vertical = 0
    for ll in lst2:
        vertical += ''.join(ll).count('vo^')

    print(horizon + vertical)
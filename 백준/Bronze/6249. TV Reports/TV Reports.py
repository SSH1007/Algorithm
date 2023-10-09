n, p, h = map(int, input().split())
for _ in range(n):
    dollar = int(input())
    if dollar > h:
        print('BBTV: Dollar reached %d Oshloobs, A record!'%dollar)
        h = dollar
    if dollar < p:
        print('NTV: Dollar dropped by %d Oshloobs'%(abs(dollar-p)))
    p = dollar
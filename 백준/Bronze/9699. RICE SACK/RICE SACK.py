T = int(input())
for t in range(1, T+1):
    sack = list(map(int, input().split()))
    print('Case #%d: %d'%(t,max(sack)))
import sys
input = sys.stdin.readline
T = int(input().rstrip())
for _ in range(T):
    dic = dict()
    a, b = map(int, input().rstrip().split())
    alst = list(map(int, input().rstrip().split()))
    for al in alst:
        if al not in dic:
            dic[al] = 1
        else:
            dic[al]+=1
    blst = list(map(int, input().rstrip().split()))
    for bl in blst:
        if bl not in dic:
            dic[bl] = 1
        else:
            dic[bl]+=1
    print(list(dic.values()).count(2))
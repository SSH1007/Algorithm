import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):
    N = int(input())
    dic = dict()
    for _ in range(N):
        name, ctgr = input().split()
        if ctgr not in dic:
            dic[ctgr] = 1
        else:
            dic[ctgr]+=1
    cnt = 1
    for v in dic.values():
        cnt*=(v+1)
    print(cnt-1)
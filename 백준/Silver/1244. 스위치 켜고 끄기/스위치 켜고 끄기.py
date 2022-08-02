import sys
input=sys.stdin.readline
swn = int(input()) # switch number
sws = list(map(int,input().split())) # switch case
stn = int(input()) # students number
for _ in range(stn):
    sex,num = map(int,input().split()) # 성별, 받은 숫자
    if sex%2: # 남
        if num>len(sws) or num<0:
            break
        for sw in range(num-1,swn,num):
            sws[sw]=abs(sws[sw]-1)
    else: # 여
        l = num-2
        r = num
        sws[num-1] = abs(sws[num-1]-1)
        while 1:
            if l<0 or r>=len(sws):
                break
            if sws[l]==sws[r]:
                sws[l]=abs(sws[l]-1)
                sws[r]=abs(sws[r]-1)
                l-=1
                r+=1
            else:
                break
for sw in range(1,swn+1):
    print(sws[sw-1], end=' ')
    if sw%20==0:
        print()
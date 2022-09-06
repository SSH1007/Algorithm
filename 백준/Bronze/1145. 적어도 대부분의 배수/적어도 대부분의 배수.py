lst = list(map(int,input().split()))
lst.sort()
start = lst[0]
while 1:
    cnt = 0
    for l in lst:
        if start%l==0:
            cnt+=1
    if cnt >= 3:
        break
    start+=1
print(start)
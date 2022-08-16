day = int(input())
lst = list(map(int,input().split()))
cnt = 0
for l in lst:
    if l == day:
        cnt+=1
print(cnt)
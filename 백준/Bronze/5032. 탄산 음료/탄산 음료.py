e,f,c=map(int,input().split())
cnt=0
ab = e+f # 모든 병 수
while 1:
    n = ab//c # 모든 병으로 교환할 수 있는 새술
    o = ab%c # 남은 빈 병들
    ab = n+o
    cnt+=n
    if ab<c:
        break
print(cnt)
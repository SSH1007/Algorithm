def two_circle(x1, y1, r1, x2, y2, r2):
    if x1==x2 and y1==y2 and r1==r2:    # 동일, 접점 무한대
        return -1
    elif (x1-x2)**2+(y1-y2)**2 == (r1+r2)**2:   # 외접
        return 1
    elif (x1-x2)**2+(y1-y2)**2 == (r1-r2)**2:   # 내접
        return 1
    elif (x1-x2)**2+(y1-y2)**2 < (r1-r2)**2:   # 내부에서 안  만남
        return 0
    elif (x1-x2)**2+(y1-y2)**2 > (r1+r2)**2:    # 둘이 멀리 떨어져 있음
        return 0
    elif x1==x2 and y1==y2 and r1!=r2:  # 원 안에 원
        return 0
    else:
        return 2
    
T = int(input())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int,input().split())
    print(two_circle(x1, y1, r1, x2, y2, r2))
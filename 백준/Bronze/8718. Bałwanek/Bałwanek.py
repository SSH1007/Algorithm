# 공원에 있는 눈의 양 x, 눈사람 공 하나의 눈의 양 k
x, k = map(int, input().split())
# k가 가장 작은 공일 때
a = k+k*2+k*4
# k가 중간 공일 때
b = k*0.5+k+k*2
# k가 가장 큰 공일 때
c = k*0.25+k*0.5+k
if a > x:
    if b > x:
        if c > x:
            print(0)
        else:
            print(int(c*1000))
    else:
        print(int(b*1000))
else:
    print(int(a*1000))    
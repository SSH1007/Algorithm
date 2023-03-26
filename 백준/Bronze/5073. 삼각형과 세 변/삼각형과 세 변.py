while 1:
    a, b, c = sorted(map(int, input().split()))
    # 마지막 줄은 0, 0, 0이며 계산하지 않는다
    if a==b==c==0:
        break
    # a,b,c가 삼각형의 조건을 만족하지 않으면 Invalid
    if a+b<=c:
        print('Invalid')
    # 삼각형의 조건을 만족하면 이하
    elif a==b==c:
        print('Equilateral')
    elif a==b or b==c or c==a:
        print('Isosceles')
    else:
        print('Scalene')
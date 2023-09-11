T = int(input())
for _ in range(T):
    height, weight = map(int, input().split())
    if height < 140.1:
        print(6)
    elif 140.1 <= height < 146:
        print(5)
    elif 146 <= height < 159:
        print(4)
    elif 159 <= height < 161:
        if 16.0 <= weight/(height*height*0.0001) < 35.0:
            print(3)
        else:
            print(4)
    elif 161 <= height < 204:
        if 20.0 <= weight/(height*height*0.0001) < 25.0:
            print(1)
        elif 18.5 <= weight/(height*height*0.0001) < 20.0 or 25.0 <= weight/(height*height*0.0001) < 30.0:
            print(2)
        elif 16.0 <= weight/(height*height*0.0001) < 18.5 or 30.0 <= weight/(height*height*0.0001) < 35.0:
            print(3)
        else:
            print(4)
    else:
        print(4)
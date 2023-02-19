lst = list(map(int, input().split()))
lst.sort()
# 만약 lst가 등차수열이라면
if lst[2]-lst[1] == lst[1]-lst[0]:
    # 제일 작은 놈이나 제일 큰 놈을 출력
    # 제일 작은 놈이 -100보다 작으면
    if lst[0]-(lst[2]-lst[1]) < -100:
        print(lst[2]+(lst[2]-lst[1]))
    # 제일 큰 놈이 100보다 크면
    elif lst[2]+(lst[2]-lst[1]) > 100:
        print(lst[0]-(lst[2]-lst[1]))
    else:
        print(lst[0]-(lst[2]-lst[1]))
else:
    if lst[2]-lst[1] > lst[1]-lst[0]:
        print(lst[1]+(lst[2]-lst[1])//2)
    else:
        print(lst[1]-(lst[1]-lst[0])//2)
def solution(a, b, c, d):
    answer = 0
    lst = [a, b, c, d]
    dic = dict()
    for l in lst:
        if not l in dic:
            dic[l] = 1
        else:
            dic[l] += 1
    arr = sorted(list(dic.items()), key = lambda x :(x[1], x[0]))
    # print(arr)
    if len(arr) == 1:
        answer = 1111*arr[0][0]
    elif len(arr) == 2:
        if arr[-1][1] == arr[0][1]:
            answer = (arr[-1][0]+arr[0][0])*abs(arr[-1][0]-arr[0][0])
        else:
            answer = (10*arr[-1][0]+arr[0][0])**2
    elif len(arr) == 3:
        answer = arr[0][0]*arr[1][0]
    else:
        answer = arr[0][0]
        
    return answer